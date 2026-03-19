import tkinter as tk
from tkinter import messagebox
import secrets
import string

FORBIDDEN_SYMBOLS = "dblLiIoO0'\""
all_chars = string.ascii_letters + string.digits + '!@$#'
allowed_chars = ''.join(c for c in all_chars if c not in FORBIDDEN_SYMBOLS)

def pass_check(password):
        has_letters = any (c in string.ascii_letters for c in password)
        has_digits = any (c in string.digits for c in password)
        has_spec = any (c in '!@$#' for c in password)
        return has_letters and has_digits and has_spec

def gen_pass():
    while True:
        password = ''.join(secrets.choice(allowed_chars) for _ in range(12))
        if pass_check(password):
            result_entry.config(state='normal')
            result_entry.delete(0, tk.END)
            result_entry.insert(0, password)
            result_entry.config(state='disabled')
            break

def copy_password():
    password = result_entry.get()

    if not password:
        messagebox.showerror("Password Error", "Generate password first")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(width=False, height=False)
tittle_label = tk.Label(root, text="Password Generator", font=("Arial", 14, "bold"))
tittle_label.pack(pady=10)


generate_button = tk.Button(root, text="Generate Password", command=gen_pass, width=20)
generate_button.pack(pady=10)

result_entry = tk.Entry(root, width=30, justify="center", font=("Arial", 12), state="readonly")
result_entry.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password, width=20)
copy_button.pack(pady=10)

root.mainloop()











