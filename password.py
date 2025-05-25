import tkinter as tk
from tkinter import messagebox
import hashlib
import json
import os

# File to store user data
USER_FILE = 'users.json'

# Load existing users
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

# Save users to file
def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f)

# Hashing password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register function
def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty!")
        return

    users = load_users()
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        users[username] = hash_password(password)
        save_users(users)
        messagebox.showinfo("Success", "Registration successful!")

# Login function
def login_user():
    username = entry_username.get()
    password = entry_password.get()
    users = load_users()

    if username in users and users[username] == hash_password(password):
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("Login Page with Password Hashing")
root.geometry("350x250")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Username:", bg="#f0f0f0", font=('Arial', 12)).pack(pady=5)
entry_username = tk.Entry(root, width=30)
entry_username.pack()

tk.Label(root, text="Password:", bg="#f0f0f0", font=('Arial', 12)).pack(pady=5)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack()

tk.Button(root, text="Login", command=login_user, bg="#4CAF50", fg="white", width=15).pack(pady=10)
tk.Button(root, text="Register", command=register_user, bg="#2196F3", fg="white", width=15).pack()

root.mainloop()
