from flask import Flask, request, redirect
import twilio.twiml
import RIPTAStopCalculations

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def echo_input():
    """Respond to incoming texts with a copy of the same text."""

    resp = twilio.twiml.Response()
    try:
        response_data = request.form.to_dict()['Body']
        # print(response_data)
    except Exception:
        response_data = Exception.__base__

    resp.message(str(response_data))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
