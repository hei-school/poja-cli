package com.company.base.endpoint;

import static com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES;
import static com.fasterxml.jackson.databind.SerializationFeature.WRITE_DATES_AS_TIMESTAMPS;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class EndpointConf {
  @Bean
  public ObjectMapper objectMapper() {
    ObjectMapper objectMapper = new ObjectMapper();
    objectMapper.configure(FAIL_ON_UNKNOWN_PROPERTIES, false);
    objectMapper.configure(WRITE_DATES_AS_TIMESTAMPS, false);
    objectMapper.findAndRegisterModules();
    return objectMapper;
  }
}
