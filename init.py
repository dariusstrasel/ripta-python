
# This script will initialise an instance of the Twilio Rest client and send a message after verifying your Twilio
# account SID and REST auth token.

from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

#TwilioRestClient _init_ callback
client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(body="Hello from Python",
        to="",    # Replace with your phone number
        from_="+17815705236") # Replace with your Twilio number
#This will print an exception if risen. Commonly returns 400, or "Invalid phone number."
except TwilioRestException as e:
    print(e)
print(message)
