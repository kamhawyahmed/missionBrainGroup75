from flask import Flask, request, render_template, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib
from twilio.twiml.messaging_response import MessagingResponse
import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(".env") #loads environ vars from .venv file (hidden on mac bc start with .)



account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

# Account SID and Auth Token from www.twilio.com/console
client = Client(account_sid,
                auth_token)

# Twilio phone number to monitor for incoming messages
twilio_phone_number = os.environ.get("twilio_phone_number")
twilio_virtual_phone_number = "+18777804236"



app = Flask(__name__)

def send_message(message_content="*** TEST MESSAGE ***"):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_content,
        from_=twilio_phone_number,
        to=twilio_virtual_phone_number,
    )

    print(message.body)
    return

def fetch_messages_to_list():
    client = Client(account_sid, auth_token)
    messages = client.messages.list(to=twilio_phone_number, limit=50)
    messages_list = []
    for message in messages:
        messages_list.append(message.body)
    return messages_list

#make sure flask running with test here
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    message = "Hello world"

    return render_template("index.html", msg=message)


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    # resp = MessagingResponse()
    prompt = fetch_messages_to_list()[0]
    send_message(message_content= f"- \n\n\n\nPatient Follow-up Services:\n\nIncoming Text: {prompt}\n\nRespone: {OpenAI.process(prompt)}")
    return "message_received"


if __name__ == '__main__':
    app.run(debug=True)
