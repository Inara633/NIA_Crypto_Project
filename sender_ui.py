import tkinter as tk
from encryption_module import generate_key, encrypt_message
from otp_module import key_to_otp
from sms_module import send_sms

def send():
    message = entry_message.get()
    phone = entry_phone.get()
    key = generate_key()
    iv, ciphertext = encrypt_message(message, key)
    otp = key_to_otp(key)
    send_sms(phone, otp)

    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, f"IV: {iv}\nEncrypted: {ciphertext}\n")

root = tk.Tk()
root.title("Sender")

tk.Label(root, text="Message:").pack()
entry_message = tk.Entry(root, width=50)
entry_message.pack()

tk.Label(root, text="Receiver Phone:").pack()
entry_phone = tk.Entry(root, width=30)
entry_phone.pack()

tk.Button(root, text="Encrypt & Send OTP", command=send).pack()

text_output = tk.Text(root, height=5, width=60)
text_output.pack()

root.mainloop()
