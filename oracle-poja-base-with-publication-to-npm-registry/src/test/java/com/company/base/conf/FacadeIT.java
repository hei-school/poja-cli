package com.company.base.conf;

import static java.lang.Runtime.getRuntime;
import static org.springframework.boot.test.context.SpringBootTest.WebEnvironment.RANDOM_PORT;

import lombok.SneakyThrows;
import org.junit.jupiter.api.BeforeAll;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;

@SpringBootTest(webEnvironment = RANDOM_PORT)
public class FacadeIT {

  private static final PostgresConf POSTGRES_CONF = new PostgresConf();
  private static final EventConf EVENT_CONF = new EventConf();

  @BeforeAll
  static void beforeAll() {
    POSTGRES_CONF.start();
    getRuntime()
        // Do _not_ stop postgresTest in afterAll as it is shared between multiple subclasses of
        // FacadeTest.
        // Doing so might cause some subclasses to stop it while other ones are still using it!
        .addShutdownHook(new Thread(POSTGRES_CONF::stop));
  }

  @SneakyThrows
  @DynamicPropertySource
  static void configureProperties(DynamicPropertyRegistry registry) {
    POSTGRES_CONF.configureProperties(registry);
    EVENT_CONF.configureProperties(registry);

    var envConfClazz = Class.forName("com.company.base.conf.EnvConf");
    var envConfConfigureProperties =
        envConfClazz.getDeclaredMethod("configureProperties", DynamicPropertyRegistry.class);
    var envConf = envConfClazz.getConstructor().newInstance();
    envConfConfigureProperties.invoke(envConf, registry);
  }
}
