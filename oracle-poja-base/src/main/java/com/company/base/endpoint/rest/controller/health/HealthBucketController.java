package com.company.base.endpoint.rest.controller.health;

import static java.io.File.createTempFile;
import static java.util.UUID.randomUUID;

import com.company.base.PojaGenerated;
import com.company.base.file.BucketComponent;
import java.io.FileWriter;
import java.io.IOException;
import java.time.Duration;
import java.util.Optional;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@PojaGenerated
@RestController
@AllArgsConstructor
public class HealthBucketController {

  BucketComponent bucketComponent;

  @GetMapping(value = "/health/bucket")
  public ResponseEntity<String> file_can_be_uploaded_then_signed() throws IOException {
    var fileSuffix = ".txt";
    var filePrefix = randomUUID().toString();
    var tmpFile = createTempFile(filePrefix, fileSuffix);
    FileWriter writer = new FileWriter(tmpFile);
    writer.write(randomUUID().toString());
    writer.close();

    var filename = filePrefix + fileSuffix;
    var bucketKey = "health/" + filename;
    bucketComponent.upload(tmpFile, bucketKey);

    return ResponseEntity.of(
        Optional.of(bucketComponent.presign(bucketKey, Duration.ofMinutes(2)).toString()));
  }
}
