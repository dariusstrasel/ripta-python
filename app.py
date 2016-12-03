from flask import Flask, request, redirect
import twilio.twiml
from flask import request

#request.headers()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    # resp.message("Hello, Mobile Monkey")
    try:
        response_data = request.form.to_dict()['body']
        print(response_data)
    except Exception:
        response_data = Exception

    resp.message(str(response_data))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# https://ancient-harbor-62057.herokuapp.com/
# https://demo.twilio.com/welcome/sms/reply/

"""ImmutableMultiDict([('NumMedia', u'0'), ('NumSegments', u'1'), ('FromZip', u'33016'), ('SmsMessageSid', u'SM6c7f8711cef645b067f55fb902bb4829'), ('Body', u'Test'), ('FromCountry', u'US'), ('To', u'+14012831818'), ('MessageSid', u'SM6c7f8711cef645b067f55fb902bb4829'), ('ApiVersion', u'2010-04-01'), ('FromState', u'FL'), ('SmsSid', u'SM6c7f8711cef645b067f55fb902bb4829'), ('ToState', u'RI'), ('ToCity', u'PROVIDENCE'), ('ToZip', u'02906'), ('ToCountry', u'US'), ('From', u'+13057074681'), ('SmsStatus', u'received'), ('AccountSid', u'AC78c549fa01a56be05531f28061f754f2'), ('FromCity', u'MIAMI')])"""