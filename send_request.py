import requests

payload = {'Body': 'blank'}
local_server = 'http://127.0.0.1:5000'
live_server = 'https://ancient-harbor-62057.herokuapp.com/'

def send_test_payload(url, payload):
    try:
        response = requests.post(url, data=payload).text
    except Exception as ex:
        template = "An exception of type {0} occured."
        message = template.format(type(ex).__name__)
        response = message
    return response

print(send_test_payload(local_server, payload))
print(send_test_payload(live_server, payload))
