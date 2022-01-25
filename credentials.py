from __future__ import annotations

email: str="youremail@provider.com"
pw: str="yourpw"
smtpserv: str="povidersmtp.email.com"
smtpport: int=12345
receiver: list[float]=["receivermail@provider.com"]
message: str= """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""