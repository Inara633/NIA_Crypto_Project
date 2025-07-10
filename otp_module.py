import random

def generate_deterministic_key(otp: str):
    # Ensure same seed always gives same key
    seed = int(otp)
    random.seed(seed)
    return bytes([random.randint(0, 255) for _ in range(16)])

def generate_otp():
    return str(random.randint(100000, 999999))
