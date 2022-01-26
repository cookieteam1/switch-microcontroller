from __future__ import annotations

message="Hey I\'m here to notify you"
email: str="youremail@provider.com"
pw: str="yourpw"
smtpserv: str="povidersmtp.email.com"
smtpport: int=12345
receiver: list[float]=["receivermail@provider.com"]
mailmessage: str= """From: From Person <{faddr}>
To: To Person <{taddr}>
Subject: SMTP e-mail test

{mess}
""".format(faddr=email,taddr=receiver[0],mess=message)