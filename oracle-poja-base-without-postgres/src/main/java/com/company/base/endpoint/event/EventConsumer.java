package com.company.base.endpoint.event;

import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import com.company.base.PojaGenerated;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.function.Consumer;
import java.util.function.Function;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.DeleteMessageRequest;

@PojaGenerated
@Component
@Slf4j
public class EventConsumer implements Consumer<List<EventConsumer.AcknowledgeableTypedEvent>> {
  private static final String DETAIL_PROPERTY = "detail";
  private static final String DETAIL_TYPE_PROPERTY = "detail-type";
  private final EventServiceInvoker eventServiceInvoker;

  public EventConsumer(EventServiceInvoker eventServiceInvoker) {
    this.eventServiceInvoker = eventServiceInvoker;
  }

  @Override
  public void accept(List<AcknowledgeableTypedEvent> ackEvents) {
    for (AcknowledgeableTypedEvent ackEvent : ackEvents) {
      eventServiceInvoker.accept(ackEvent.getEvent());
      ackEvent.ack();
    }
  }

  @AllArgsConstructor
  public static class AcknowledgeableTypedEvent {
    @Getter private final TypedEvent event;
    private final Runnable acknowledger;

    public void ack() {
      acknowledger.run();
    }
  }

  @Component
  @AllArgsConstructor
  public static class SqsMessageAckTyper
      implements Function<List<SQSEvent.SQSMessage>, List<AcknowledgeableTypedEvent>> {
    private final EventConf eventConf;
    private final SqsClient sqsClient;
    private final ObjectMapper om;

    @Override
    public List<AcknowledgeableTypedEvent> apply(List<SQSEvent.SQSMessage> sqsMessages) {
      return toAcknowledgeableEvent(sqsMessages);
    }

    public List<AcknowledgeableTypedEvent> toAcknowledgeableEvent(
        List<SQSEvent.SQSMessage> messages) {
      var res = new ArrayList<AcknowledgeableTypedEvent>();
      for (SQSEvent.SQSMessage message : messages) {
        TypedEvent typedEvent;
        try {
          typedEvent = toTypedEvent(message);
        } catch (Exception e) {
          log.error(e.getMessage());
          log.error("Message could not be unmarshalled, message : {} \n", message);
          continue;
        }
        AcknowledgeableTypedEvent acknowledgeableTypedEvent =
            new AcknowledgeableTypedEvent(
                typedEvent,
                () ->
                    sqsClient.deleteMessage(
                        DeleteMessageRequest.builder()
                            .queueUrl(eventConf.getSqsQueue())
                            .receiptHandle(message.getReceiptHandle())
                            .build()));
        res.add(acknowledgeableTypedEvent);
      }
      return res;
    }

    @SneakyThrows
    private TypedEvent toTypedEvent(SQSEvent.SQSMessage message) {
      TypeReference<Map<String, Object>> typeRef = new TypeReference<>() {};
      Map<String, Object> body = om.readValue(message.getBody(), typeRef);
      String typeName = body.get(DETAIL_TYPE_PROPERTY).toString();
      return new TypedEvent(
          typeName, om.convertValue(body.get(DETAIL_PROPERTY), Class.forName(typeName)));
    }
  }

  public record TypedEvent(String typeName, Object payload) {}
}
