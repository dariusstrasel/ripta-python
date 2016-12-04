from flask import Flask, request
import twilio.twiml
import RIPTAStopCalculations

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def echo_input():
    """Respond to incoming texts with a copy of the same text."""

    resp = twilio.twiml.Response()
    try:
        response_data = int(request.form.to_dict()['Body'])
        # print(response_data)
    except Exception:
        response_data = Exception.__base__

    stop_distance = RIPTAStopCalculations.smsReply(response_data)

    resp.message(str(stop_distance))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
