package com.company.base;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import com.company.base.endpoint.event.EventConsumer;
import java.util.List;
import java.util.Map;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.SpringApplication;
import org.springframework.context.ConfigurableApplicationContext;

@Slf4j
@PojaGenerated
public class MailboxEventHandler implements RequestHandler<SQSEvent, String> {

  public static final String SPRING_SERVER_PORT_FOR_RANDOM_VALUE = "0";

  @Override
  public String handleRequest(SQSEvent event, Context context) {
    log.info("Received: event={}, awsReqId={}", event, context.getAwsRequestId());
    List<SQSEvent.SQSMessage> messages = event.getRecords();
    log.info("SQS messages: {}", messages);

    ConfigurableApplicationContext applicationContext = applicationContext();
    EventConsumer eventConsumer = applicationContext.getBean(EventConsumer.class);
    EventConsumer.SqsMessageAckTyper messageConverter =
        applicationContext.getBean(EventConsumer.SqsMessageAckTyper.class);

    eventConsumer.accept(messageConverter.toAcknowledgeableEvent(messages));

    applicationContext.close();
    return "ok";
  }

  private ConfigurableApplicationContext applicationContext(String... args) {
    SpringApplication application = new SpringApplication(PojaApplication.class);
    application.setDefaultProperties(
        Map.of(
            "spring.flyway.enabled", "false", "server.port", SPRING_SERVER_PORT_FOR_RANDOM_VALUE));
    return application.run(args);
  }
}
