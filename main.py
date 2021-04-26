from secrets import TWILIO_TOKEN, TWILIO_ACC_SID, TWILIO_PHONE_NO
import logging
from twilio.rest import Client

logging.basicConfig(level=logging.INFO, filename="app.log")


def main():
    client = Client(TWILIO_ACC_SID, TWILIO_TOKEN)

    message = client.messages.create(
        body="This is my first test SMS message",
        from_= TWILIO_PHONE_NO,
        to=DESTINATION_NO
    )

    print(message.sid)

if __name__ == '__main__':
    main()

# logging.debug(stuff)
