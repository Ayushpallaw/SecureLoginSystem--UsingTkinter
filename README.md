# 🔐 Secure Login System – Using Tkinter  
### A simple GUI-based login system with secure password hashing using Python and SHA-256

---

## 📝 Project Overview  
This project is a lightweight **Login System** built using **Python** and the standard `hashlib` library. It uses a simple **Graphical User Interface (GUI)** designed with `Tkinter`, enabling users to register and log in securely. Passwords are never stored in plain text — they are hashed using the **SHA-256 algorithm** for basic security compliance.

---

## 🎯 Objectives  

### 🔑 Secure Login & Registration:  
- Allow users to **register with a username and password**.  
- **Hash the password** using SHA-256 before saving.  
- Store user credentials in a **local file (`users.txt`)**.  
- Validate login by comparing input hash with stored hash.  
- Display popups for **login success**, **errors**, and **registration feedback**.

### 🖥️ GUI Features:  
- Clean and minimal interface using Python’s `Tkinter`.  
- Fields for entering **Username** and **Password**.  
- Buttons for **Login** and **Register** actions.  
- Message boxes to show **status messages** or **alerts**.

---

## 🔍 Key Insights  

- Uses **Python’s built-in `hashlib` module** – no third-party library required.  
- Passwords are **securely hashed**, not stored in plain text.  
- Ideal for small desktop apps, learning authentication flow, or prototype systems.  
- **Easy to upgrade** with persistent database (e.g., SQLite) or cloud storage.  
- Ensures basic **data protection and user management** using local files.

---

## 💡 Recommendations  

### 🌟 Feature Enhancements:  
- Add **password visibility toggle** (show/hide password).  
- Store data in **JSON or SQLite** instead of `.txt`.  
- Add **user role-based login** (admin, user).  
- Implement **"Forgot Password?"** recovery option.  
- Improve UI with **custom themes or animations**.

### 🧠 Usability Improvements:  
- Display **error highlights** on empty fields.  
- Add **keyboard shortcut support** for login (e.g., Enter key).  
- Remember previously entered username.  
- Welcome screen after login with username.

### 📦 Code Optimization:  
- Split into **modules**: `gui.py`, `auth.py`, `storage.py`.  
- Use **object-oriented programming** to organize code.  
- Add **unit tests** for hashing, login, and file operations.  
- Implement **exception logging** for better error handling.

---

## ✅ Conclusion  
The **Secure Login System** is a beginner-friendly project that showcases how to combine **Python’s GUI capabilities** with **data security fundamentals** like password hashing. It's perfect for students and hobbyists learning about user authentication, file handling, and GUI app development. With minor upgrades, it can evolve into a secure and scalable login system for personal projects.

---
