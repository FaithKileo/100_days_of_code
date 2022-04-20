import requests

# importing twilio - Make sure to install twilio with pip install twilio
from twilio.rest import Client

# initialize a twilio client
client = Client("AC7580b24a06fffa8ca4d762c5c9053901", "c975a5ce350454548a4bfb07464da76b")

def jack_send_sms(to, msg: str):
    try:
        for t in to.split(","):
            message = client.messages \
                        .create(
                            body=msg,
                            from_='+12182858596',
                            to=t.strip()
                        )
            print(f"Sending sms to "+t)
    except:
        return "send failed"
    

err = jack_send_sms("+255712111936","Faith")
print(err)
# print("hgdfhjjkdf")
