import requests

def send_sms(phone_number, otp):
    sender_name = "inara"
    message = f"[{sender_name}] Your OTP is: {otp}. Reply STOP to opt-out."

    resp = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': message,
        'key': '9d4b615316ac1942f632cf211f23f66a6458ae0cQTXI0gJEiB4q5j0cF0dOYdJwF'  # Replace with your paid key
    })

    print("SMS API response:", resp.json())
    return resp.json()
