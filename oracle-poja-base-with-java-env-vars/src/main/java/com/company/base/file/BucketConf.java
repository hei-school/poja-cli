package com.company.base.file;

import com.company.base.PojaGenerated;
import lombok.Getter;
import lombok.SneakyThrows;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3AsyncClient;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;
import software.amazon.awssdk.transfer.s3.S3TransferManager;

@PojaGenerated
@Configuration
public class BucketConf {

  @Getter private final String bucketName;
  @Getter private final S3TransferManager s3TransferManager;
  @Getter private final S3Presigner s3Presigner;

  @SneakyThrows
  public BucketConf(
      @Value("${aws.region}") String regionString, @Value("${aws.s3.bucket}") String bucketName) {
    this.bucketName = bucketName;
    var region = Region.of(regionString);
    this.s3TransferManager =
        S3TransferManager.builder()
            .s3Client(S3AsyncClient.crtBuilder().region(region).build())
            .build();
    this.s3Presigner = S3Presigner.builder().region(region).build();
  }
}
