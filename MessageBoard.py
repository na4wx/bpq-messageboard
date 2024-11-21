#!/usr/bin/env python3

import sys
import os
from datetime import datetime

# This script was developed by Jordan Webb, NA4WX, using the MIT License. Edit, Share, Enjoy. Just Keep this line here.

# Database files
USER_DB = "users.txt"
MESSAGE_DB = "messages.txt"

# Load users from the database
def load_users():
    users = {}
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as f:
            for line in f:
                callsign, username, location, last_login = line.strip().split(",")
                users[callsign] = {
                    "username": username,
                    "location": location,
                    "last_login": last_login,
                }
    return users

# Save users to the database
def save_users(users):
    with open(USER_DB, "w") as f:
        for callsign, data in users.items():
            f.write(f"{callsign},{data['username']},{data['location']},{data['last_login']}\n")

# Load messages from the database
def load_messages():
    if os.path.exists(MESSAGE_DB):
        with open(MESSAGE_DB, "r") as f:
            return [line.strip() for line in f]
    return []

# Save messages to the database
def save_messages(messages):
    with open(MESSAGE_DB, "w") as f:
        f.write("\n".join(messages) + "\n")

# Display the main menu
def main_menu():
    sys.stdout.write("\nMessage Board Menu:\n")
    sys.stdout.write("1. View Messages\n")
    sys.stdout.write("2. Post a Message\n")
    sys.stdout.write("3. Change Username or Location\n")
    sys.stdout.write("4. Quit\n")
    sys.stdout.write("Enter your choice: ")
    sys.stdout.flush()
    return sys.stdin.readline().strip()

# Handle a user's session
def handle_user_session():
    sys.stdout.write("Welcome to the BPQ Message Board!\n")
    sys.stdout.write("Enter your callsign: ")
    sys.stdout.flush()

    # Get callsign from user input
    callsign = sys.stdin.readline().strip().upper()
    if not callsign:
        sys.stdout.write("Error: Callsign not provided. Disconnecting.\n")
        sys.stdout.flush()
        return

    # Load users and handle login
    users = load_users()
    if callsign in users:
        user = users[callsign]
        user["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sys.stdout.write(f"Welcome back, {user['username']} ({callsign})!\n")
    else:
        sys.stdout.write("New user detected! Creating profile...\n")
        sys.stdout.write("Enter your username: ")
        sys.stdout.flush()
        username = sys.stdin.readline().strip()
        sys.stdout.write("Enter your location: ")
        sys.stdout.flush()
        location = sys.stdin.readline().strip()
        user = {
            "username": username,
            "location": location,
            "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        users[callsign] = user
        save_users(users)
        sys.stdout.write("Profile created successfully!\n")

    # Main menu loop
    while True:
        choice = main_menu()
        if choice == "1":
            # View messages
            messages = load_messages()
            if messages:
                sys.stdout.write("\nMessages:\n")
                for msg in messages:
                    sys.stdout.write(f"{msg}\n")
            else:
                sys.stdout.write("\nNo messages available.\n")
        elif choice == "2":
            # Post a message
            sys.stdout.write("Enter your message: ")
            sys.stdout.flush()
            message = sys.stdin.readline().strip()
            if message:
                messages = load_messages()
                messages.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {user['username']} ({callsign}): {message}")
                save_messages(messages)
                sys.stdout.write("Message posted successfully!\n")
            else:
                sys.stdout.write("Message cannot be empty.\n")
        elif choice == "3":
            # Change username or location
            sys.stdout.write("Enter new username (leave blank to keep current): ")
            sys.stdout.flush()
            new_username = sys.stdin.readline().strip()
            sys.stdout.write("Enter new location (leave blank to keep current): ")
            sys.stdout.flush()
            new_location = sys.stdin.readline().strip()
            if new_username:
                user["username"] = new_username
            if new_location:
                user["location"] = new_location
            save_users(users)
            sys.stdout.write("Profile updated successfully!\n")
        elif choice == "4":
            # Quit
            sys.stdout.write("Goodbye!\n")
            sys.stdout.flush()
            break
        else:
            sys.stdout.write("Invalid choice. Please try again.\n")
        sys.stdout.flush()

if __name__ == "__main__":
    handle_user_session()
