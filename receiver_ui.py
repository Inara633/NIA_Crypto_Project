# receiver_ui.py
import tkinter as tk
from encryption_module import decrypt_message
from otp_module import generate_deterministic_key

def decrypt():
    otp = entry_otp.get()
    iv = entry_iv.get()
    encrypted = entry_cipher.get()

    if not otp or not iv or not encrypted:
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, "Please fill in all fields.")
        return

    try:
        key = generate_deterministic_key(otp)
        message = decrypt_message(iv, encrypted, key)
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, f"Decrypted Message:\n{message}")
    except Exception as e:
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, f"Decryption failed. Error: {str(e)}")

# Tkinter GUI setup
root = tk.Tk()
root.title("AES Receiver")

tk.Label(root, text="IV (from sender):").pack()
entry_iv = tk.Entry(root, width=80)
entry_iv.pack(pady=2)

tk.Label(root, text="Encrypted Message:").pack()
entry_cipher = tk.Entry(root, width=80)
entry_cipher.pack(pady=2)

tk.Label(root, text="Enter OTP:").pack()
entry_otp = tk.Entry(root, width=20)
entry_otp.pack(pady=2)

tk.Button(root, text="Decrypt Message", command=decrypt).pack(pady=5)

text_output = tk.Text(root, height=10, width=80)
text_output.pack(pady=5)

root.mainloop()
