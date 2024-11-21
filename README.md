# 📬 BPQ32 Message Board (messageboard.py)

Welcome to **BPQ32 Message Board**, a Python-based application designed to integrate seamlessly with **BPQ32** for hosting a message board system. This script allows users to post, view, and manage messages, along with customizing their profiles directly through a Telnet interface. 🚀

---

## 🌟 Features

- **User Profile Management**  
  Automatically detects new users and creates profiles with username and location. Updates user details via a menu-driven interface.
  
- **Message Posting**  
  Allows users to post messages to a shared board. Messages include timestamps, username, and callsign.
  
- **Message Viewing**  
  Displays all messages in a scrollable format.
  
- **Persistent Storage**  
  Stores user data and messages in text-based databases for easy management.
  
- **Telnet Integration**  
  Designed to work with BPQ32 using **inetd** to manage connections.

---

## 🛠️ Requirements

- **Python**: Version 3.6 or later.
- **BPQ32**: Configured to pass connections to the script via Telnet.
- **Text-based Databases**:
  - `users.txt`: Stores user profiles.
  - `messages.txt`: Stores posted messages.

---

## 📂 File Structure

```plaintext
.
├── messageboard.py        # Main Python script
├── users.txt              # User database (auto-generated)
├── messages.txt           # Message database (auto-generated)
