package com.company.base.unit.objectMapper;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.time.Instant;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
public class SomeClassWithDatetimeField {
  @JsonProperty("datetimeField")
  private Instant datetimeField;

  public String toJsonString() {
    return "{\"datetimeField\": \" " + this.datetimeField + "\"}";
  }
}
