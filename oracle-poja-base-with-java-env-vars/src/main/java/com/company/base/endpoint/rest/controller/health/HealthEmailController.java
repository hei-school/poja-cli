package com.company.base.endpoint.rest.controller.health;

import static com.company.base.endpoint.rest.controller.health.PingController.OK;
import static java.io.File.createTempFile;

import com.company.base.PojaGenerated;
import com.company.base.mail.Email;
import com.company.base.mail.Mailer;
import jakarta.mail.internet.AddressException;
import jakarta.mail.internet.InternetAddress;
import java.io.IOException;
import java.util.List;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@PojaGenerated
@RestController
@AllArgsConstructor
public class HealthEmailController {

  Mailer mailer;

  @GetMapping(value = "/health/email")
  public ResponseEntity<String> send_emails(@RequestParam String to)
      throws AddressException, IOException {
    var toInternetAddress = new InternetAddress(to);
    mailer.accept(
        new Email(
            toInternetAddress,
            List.of(),
            List.of(),
            "[poja health check 1/5] Subject only",
            null,
            List.of()));

    var emailParts = to.split("@");
    var emailUser = emailParts[0];
    var emailDomain = "@" + emailParts[1];
    mailer.accept(
        new Email(
            toInternetAddress,
            List.of(new InternetAddress(emailUser + "+cc" + emailDomain)),
            List.of(),
            "[poja health check 2/5] With cc",
            null,
            List.of()));

    mailer.accept(
        new Email(
            toInternetAddress,
            List.of(),
            List.of(new InternetAddress(emailUser + "+bcc" + emailDomain)),
            "[poja health check 3/5] With bcc",
            null,
            List.of()));

    mailer.accept(
        new Email(
            toInternetAddress,
            List.of(),
            List.of(),
            "[poja health check 4/5] With body",
            "<span><b>Hello!</b></span>",
            List.of()));

    mailer.accept(
        new Email(
            toInternetAddress,
            List.of(),
            List.of(),
            "[poja health check 5/5] With attachment",
            null,
            List.of(createTempFile("attachment", ".txt"))));
    return OK;
  }
}
