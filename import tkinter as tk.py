import tkinter as tk
from encryption_module import decrypt_message
from otp_module import otp_to_key

def decrypt():
    otp = entry_otp.get()
    iv = entry_iv.get()
    encrypted = entry_cipher.get()

    key = otp_to_key(otp)
    try:
        message = decrypt_message(iv, encrypted, key)
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, f"Decrypted Message: {message}")
    except:
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, "Decryption failed. Check OTP or ciphertext.")

root = tk.Tk()
root.title("Receiver")

tk.Label(root, text="IV (from sender):").pack()
entry_iv = tk.Entry(root, width=50)
entry_iv.pack()

tk.Label(root, text="Encrypted Message:").pack()
entry_cipher = tk.Entry(root, width=50)
entry_cipher.pack()

tk.Label(root, text="Enter OTP:").pack()
entry_otp = tk.Entry(root, width=20)
entry_otp.pack()

tk.Button(root, text="Decrypt", command=decrypt).pack()

text_output = tk.Text(root, height=5, width=60)
text_output.pack()

root.mainloop()
