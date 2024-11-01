import os
from twilio.rest import Client
from flask import Flask, request

app = Flask(__name__)

# Your Twilio account SID and auth token
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    # Extract incoming message details
    from_number = request.form['From']
    message_body = request.form['Body']

    # Process the message and send a response
    response_message = f"You said: {message_body}"
    message = client.messages.create(
        body=response_message,
        from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
        to=from_number
    )
    return 'OK', 200

if __name__ == '__main__':
    app.run()