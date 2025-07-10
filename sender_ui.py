# sender_ui.py
import tkinter as tk
from encryption_module import encrypt_message
from otp_module import generate_otp, generate_deterministic_key
from sms_module import send_sms

def send():
    message = entry_message.get()
    phone = entry_phone.get()

    if not message or not phone:
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, "Please enter both message and phone number.")
        return

    otp = generate_otp()
    key = generate_deterministic_key(otp)
    iv, ciphertext = encrypt_message(message, key)

    # Silently send the OTP via SMS
    send_sms(phone, otp)

    # Display only the IV and encrypted message
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, f"Message encrypted successfully.\n\n")
    text_output.insert(tk.END, f"IV:\n{iv}\n\n")
    text_output.insert(tk.END, f"Encrypted Message:\n{ciphertext}")

# Tkinter GUI setup
root = tk.Tk()
root.title("AES Sender")

tk.Label(root, text="Message to Encrypt:").pack()
entry_message = tk.Entry(root, width=60)
entry_message.pack(pady=2)

tk.Label(root, text="Receiver Phone Number:").pack()
entry_phone = tk.Entry(root, width=30)
entry_phone.pack(pady=2)

tk.Button(root, text="Encrypt & Send OTP", command=send).pack(pady=5)

text_output = tk.Text(root, height=10, width=80)
text_output.pack(pady=5)

root.mainloop()
