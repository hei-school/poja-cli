package com.company.base.mail;

import com.company.base.PojaGenerated;
import lombok.Getter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ses.SesClient;

@PojaGenerated
@Configuration
public class EmailConf {

  @Getter private final String sesSource;
  private final Region region;

  public EmailConf(
      @Value("${aws.ses.source}") String sesSource, @Value("eu-west-3") Region region) {
    this.sesSource = sesSource;
    this.region = region;
  }

  @Bean
  public SesClient getSesClient() {
    return SesClient.builder().region(region).build();
  }
}
