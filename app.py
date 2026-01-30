"""
Weekly Travel Schedule Texter

Sends your girlfriend a text every Monday with your upcoming
weekend work travel schedule + a motivational quote.

Usage:
  python app.py          # Send the text now (for testing)
  python app.py --cron   # Run on a loop, sends every Monday at 8:00 AM
"""

import os
import sys
import time

import schedule as sched
from dotenv import load_dotenv
from twilio.rest import Client

from quotes import get_random_quote
from schedule_data import TRAVEL_SCHEDULE

load_dotenv()

TWILIO_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_NUMBER = os.environ["TWILIO_PHONE_NUMBER"]
TO_NUMBER = os.environ["GIRLFRIEND_PHONE_NUMBER"]


def build_message():
    """Build the weekly text message."""
    quote_text, author = get_random_quote()

    lines = ["Hey babe! Here's my weekend work travel schedule:\n"]

    if TRAVEL_SCHEDULE:
        for trip in TRAVEL_SCHEDULE:
            lines.append(f"📅 {trip['dates']}")
            lines.append(f"📍 {trip['location']}")
            lines.append(f"💼 {trip['purpose']}\n")
    else:
        lines.append("No travel this weekend — I'm all yours! 🏠\n")

    lines.append(f'"{quote_text}"\n— {author}')
    lines.append("\nLove you ❤️")

    return "\n".join(lines)


def send_text():
    """Send the schedule text via Twilio."""
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    body = build_message()
    message = client.messages.create(
        body=body,
        from_=TWILIO_NUMBER,
        to=TO_NUMBER,
    )
    print(f"Message sent! SID: {message.sid}")


def run_scheduler():
    """Run on a loop, sending every Monday at 8 AM."""
    sched.every().monday.at("08:00").do(send_text)
    print("Scheduler running. Will text every Monday at 8:00 AM.")
    while True:
        sched.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    if "--cron" in sys.argv:
        run_scheduler()
    else:
        send_text()
