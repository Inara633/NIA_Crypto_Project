import requests

def send_sms(phone_number, otp):
    response = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': f'Your OTP for decryption is: {otp}',
        'key': 'textbelt',  # Free key for testing
    })
    print("SMS API response:", response.json())
    return response.json()
