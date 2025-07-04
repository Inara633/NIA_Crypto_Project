from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64
from Crypto.Util.Padding import unpad
def generate_key():
    return get_random_bytes(16)  # AES-128

def encrypt_message(message, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_msg = pad(message.encode(), AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_msg)
    # Encode to Base64 for easy transmission
    return base64.b64encode(iv).decode(), base64.b64encode(encrypted_bytes).decode()

def decrypt_message(iv_b64, encrypted_b64, key):
    iv = base64.b64decode(iv_b64)
    encrypted_data = base64.b64decode(encrypted_b64)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted_data)
    return unpad(decrypted_padded, AES.block_size).decode()
