from src.messages.wordle.constants import NOTIFICATIONS_SENDER_EMAIL, GMAIL_SCOPES, GMAIL_API_SECRETS
from google.oauth2 import service_account
from googleapiclient.discovery import build

def create_gmail_service():
    credentials = service_account.Credentials.from_service_account_info(
        GMAIL_API_SECRETS, scopes=GMAIL_SCOPES
    ).with_subject(NOTIFICATIONS_SENDER_EMAIL)

    return build("gmail", "v1", credentials=credentials)

def get_gmail_signature(service, user_id="me"):
    send_as_settings = service.users().settings().sendAs().list(userId=user_id).execute()
    for send_as in send_as_settings.get("sendAs", []):
        if send_as.get("isDefault"):  
            return send_as.get("signature", "")
    return ""

def build_html_with_gmail_signature(greeting: str, body_text: str, signature: str) -> str:
    return f"""
    <html>
      <body>
        {greeting}
        <p>{body_text}</p>
        {signature if signature else ""}
      </body>
    </html>
    """

