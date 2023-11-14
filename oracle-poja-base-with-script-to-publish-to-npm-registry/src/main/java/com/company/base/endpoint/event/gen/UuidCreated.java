package com.company.base.endpoint.event.gen;

import com.company.base.PojaGenerated;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.io.Serializable;
import javax.annotation.processing.Generated;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

@PojaGenerated
@Generated("EventBridge")
@NoArgsConstructor
@AllArgsConstructor
@Builder(toBuilder = true)
@Data
@EqualsAndHashCode
@ToString
public class UuidCreated implements Serializable {
  @JsonProperty("uuid")
  private String uuid;
}
