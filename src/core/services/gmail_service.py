import aiosmtplib
from email.message import EmailMessage

from src.core.configs.config import settings


class GmailSender:

    async def send_verification_email(self, to: str, code: str):
        msg = EmailMessage()
        msg["From"] = settings.GMAIL_FROM.get_secret_value()
        msg["To"] = to
        msg["Subject"] = "Account confirmation"
        msg.set_content(f"Your verification code: {code}")

        await aiosmtplib.send(
            msg,
            hostname="smtp.gmail.com",
            port=587,
            start_tls=True,
            username=settings.GMAIL_USERNAME.get_secret_value(),
            password=settings.GMAIL_PASSWORD.get_secret_value(),
        )
