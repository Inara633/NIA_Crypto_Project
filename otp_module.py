import random

def key_to_otp(key):
    return ''.join(str(b).zfill(3) for b in key)[:6]  # Convert to 6-digit OTP

def otp_to_key(otp):
    seed = int(otp) * 123456  # Deterministic method
    random.seed(seed)
    return bytes([random.randint(0, 255) for _ in range(16)])
