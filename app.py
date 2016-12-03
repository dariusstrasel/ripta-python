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
    resp.message(str(request))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# https://ancient-harbor-62057.herokuapp.com/
# https://demo.twilio.com/welcome/sms/reply/