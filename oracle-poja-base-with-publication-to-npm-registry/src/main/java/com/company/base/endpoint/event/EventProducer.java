package com.company.base.endpoint.event;

import com.company.base.PojaGenerated;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.stereotype.Component;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.eventbridge.EventBridgeClient;
import software.amazon.awssdk.services.eventbridge.model.PutEventsRequest;
import software.amazon.awssdk.services.eventbridge.model.PutEventsRequestEntry;
import software.amazon.awssdk.services.eventbridge.model.PutEventsResponse;
import software.amazon.awssdk.services.eventbridge.model.PutEventsResultEntry;

@PojaGenerated
@Component
@Slf4j
public class EventProducer implements Consumer<List<Object>> {
  private static final String EVENT_SOURCE = "com.company.base";
  private final ObjectMapper om;
  private final String eventBusName;
  private final EventBridgeClient eventBridgeClient;

  public EventProducer(
      ObjectMapper om,
      @Value("${aws.eventBridge.bus}") String eventBusName,
      EventBridgeClient eventBridgeClient) {
    this.om = om;
    this.eventBusName = eventBusName;
    this.eventBridgeClient = eventBridgeClient;
  }

  @Override
  public void accept(List<Object> events) {
    log.info("Events to send {}", events);
    PutEventsResponse response = sendRequest(events);
    checkResponse(response);
  }

  private PutEventsRequest toEventsRequest(List<Object> events) {
    return PutEventsRequest.builder()
        .entries(events.stream().map(this::toRequestEntry).toList())
        .build();
  }

  private PutEventsRequestEntry toRequestEntry(Object event) {
    try {
      String eventAsString = om.writeValueAsString(event);
      return PutEventsRequestEntry.builder()
          .source(EVENT_SOURCE)
          .detailType(event.getClass().getTypeName())
          .detail(eventAsString)
          .eventBusName(eventBusName)
          .build();
    } catch (JsonProcessingException e) {
      throw new RuntimeException(e);
    }
  }

  private PutEventsResponse sendRequest(List<Object> events) {
    checkPayload(events);
    PutEventsRequest eventsRequest = toEventsRequest(events);
    return eventBridgeClient.putEvents(eventsRequest);
  }

  private boolean isPayloadValid(List<Object> events) {
    PutEventsRequest eventsRequest = toEventsRequest(events);
    return eventsRequest.entries().size() <= Conf.MAX_PUT_EVENT_ENTRIES;
  }

  private void checkPayload(List<Object> events) {
    if (!isPayloadValid(events)) {
      throw new RuntimeException("Request entries must be <= " + Conf.MAX_PUT_EVENT_ENTRIES);
    }
  }

  private void checkResponse(PutEventsResponse response) {
    List<PutEventsResultEntry> failedEntries = new ArrayList<>();
    List<PutEventsResultEntry> successfulEntries = new ArrayList<>();

    for (PutEventsResultEntry resultEntry : response.entries()) {
      if (resultEntry.eventId() == null) {
        failedEntries.add(resultEntry);
      }
      successfulEntries.add(resultEntry);
    }

    if (!failedEntries.isEmpty()) {
      log.error("Following events were not successfully sent: {}", failedEntries);
    }
    if (!successfulEntries.isEmpty()) {
      log.info("Following events were successfully sent: {}", successfulEntries);
    }
  }

  @Configuration
  public static class Conf {
    public static final int MAX_PUT_EVENT_ENTRIES = 10;
    private final Region region;

    public Conf(@Value("${aws.region}") String region) {
      this.region = Region.of(region);
    }

    @Bean
    public EventBridgeClient getEventBridgeClient() {
      return EventBridgeClient.builder().region(region).build();
    }
  }
}
