from src.messages.wordle.constants import NOTIFICATIONS_SENDER_EMAIL, GMAIL_DISPLAY_NAME
from src.messages.wordle.utils import create_gmail_service, get_gmail_signature, build_html_with_gmail_signature
from src.messages.wordle.message_templates import MessageBodies, MessageSubjects, MessageGreetings
from email.message import EmailMessage
import base64


def send_reminder_via_gmail(recipient_email: str, recipient_name: str):
    service = create_gmail_service()
    html_signature = get_gmail_signature(service)
    html_signature = build_html_with_gmail_signature(
        MessageGreetings.ITS_BEEN_A_WHILE.format(user_name=recipient_name),
        MessageBodies.ITS_BEEN_A_WHILE, html_signature
    )
    message = EmailMessage()
    message["To"] = recipient_email
    message["From"] = f"{GMAIL_DISPLAY_NAME} <{NOTIFICATIONS_SENDER_EMAIL}>"
    message["Subject"] = MessageSubjects.ITS_BEEN_A_WHILE
    message.add_alternative(html_signature, subtype='html')

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    create_message = {"raw": encoded_message}

    sent_message = service.users().messages().send(userId="me", body=create_message).execute()

    return sent_message.get("id") if sent_message.get("id") else None