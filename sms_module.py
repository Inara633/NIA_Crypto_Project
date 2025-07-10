import requests

# Replace these with your actual Infobip account values
BASE_URL = "https://4epqym.api.infobip.com"  # Use your real Infobip base URL
API_KEY = "b915269f7ca3fe54fba60cbcd3e5ec49-bcc63ba6-63b6-4c1e-a353-6820af4f3b09"
SENDER_ID = "Inara"  # Appears in SMS on supported networks

def send_sms(phone_number, otp):
    url = f"{BASE_URL}/sms/2/text/advanced"
    
    headers = {
        "Authorization": f"App {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "messages": [
            {
                "from": SENDER_ID,
                "destinations": [{"to": phone_number}],
                "text": f"[CryptoApp] Your OTP is: {otp}. Reply STOP to opt-out."
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
    
    print("SMS API response:", response.json())

    return response.json()
