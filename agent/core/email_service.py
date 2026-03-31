import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from core.config import settings


def build_email_html(
    agent_type: str,
    user_name: str,
    event_context: dict,
    personalization_answers: dict,
    selected_venue: dict | None,
    selected_menu: str | None,
) -> str:
    event_label = agent_type.replace("_", " ").title()

    rows = ""

    # Event context rows
    for key, val in event_context.items():
        if val:
            rows += f"<tr><td><b>{key.replace('_', ' ').title()}</b></td><td>{val}</td></tr>"

    # Selected venue
    if selected_venue:
        venue_name = selected_venue.get("name", "N/A")
        venue_city = selected_venue.get("city", "")
        rows += f"<tr><td><b>Selected Venue</b></td><td>{venue_name}, {venue_city}</td></tr>"

    # Selected menu
    if selected_menu:
        rows += f"<tr><td><b>Selected Menu</b></td><td>{selected_menu}</td></tr>"

    # Personalization answers
    if personalization_answers:
        rows += '<tr><td colspan="2"><b style="font-size:15px;">Personalization Answers</b></td></tr>'
        for question, answer in personalization_answers.items():
            rows += f"<tr><td style='padding-left:16px'>{question}</td><td>{answer}</td></tr>"

    return f"""
    <html><body style="font-family: Arial, sans-serif; color: #222;">
    <h2 style="color:#1a1a1a;">New {event_label} Inquiry — {user_name}</h2>
    <p>A new corporate event inquiry has been received via LuxeVenue AI Concierge.</p>
    <table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse;width:100%;max-width:700px;">
      <thead>
        <tr style="background:#1a1a1a;color:white;">
          <th style="width:35%">Field</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
    <p style="color:#888;font-size:12px;margin-top:20px;">Sent by LuxeVenue AI Concierge &mdash; luxevenue.ai</p>
    </body></html>
    """


def send_inquiry_email(
    agent_type: str,
    user_name: str,
    event_context: dict,
    personalization_answers: dict,
    selected_venue: dict | None = None,
    selected_menu: str | None = None,
) -> bool:
    try:
        event_label = agent_type.replace("_", " ").title()
        subject = f"[LuxeVenue] New {event_label} Inquiry — {user_name}"

        html_body = build_email_html(
            agent_type=agent_type,
            user_name=user_name,
            event_context=event_context,
            personalization_answers=personalization_answers,
            selected_venue=selected_venue,
            selected_menu=selected_menu,
        )

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = settings.smtp_sender_email
        msg["To"] = "ronit@luxevenue.ai"
        msg.attach(MIMEText(html_body, "html"))

        with smtplib.SMTP_SSL(settings.smtp_host, settings.smtp_port) as server:
            server.login(settings.smtp_sender_email, settings.smtp_app_password)
            server.sendmail(settings.smtp_sender_email, "ronit@luxevenue.ai", msg.as_string())

        return True
    except Exception as e:
        print(f"[Email] Failed to send: {e}")
        return False
