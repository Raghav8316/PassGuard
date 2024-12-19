import tkinter as tk  # for GUI interface
from tkinter import StringVar, ttk  # for dynamic text and progress bar
import re  # for regular expressions  like finding special characters (@, #)
import secrets  # for random password generation
import hashlib  # for hashing (pass to a hash)
import requests  # for API calls
feedback = []

# Function to assess password strength
def assess_password_strength(password):
    score = 0  # higher score = stronger password (Scoring a password like grading homework.
                             #Each rule followed gives marks (points).)
    feedback = []  # stores suggestions for improvement

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 chars).")

      # Ensures a mix of uppercase and lowercase letters:
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

      #Checks for numbers like "123". Think of adding variety to make passwords harder to guess:
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one numeric character.")

        #Searches for special characters like “@” or “#”:
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include special characters (e.g., !, @, #).")

    #Prevents too many repeats like "aaaa1111":
    if len(set(password)) / len(password) > 0.7:
        score += 1
    else:
        feedback.append("Avoid too many repeating characters.")

    #Assigns labels like “Weak” or “Very Strong:
    strength = 'Weak'
    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"

    return score, strength, feedback


def update_feedback(event):
    password = password_var.get()
    if password == "":
        strength_label_var.set("Strength: ")
        strength_progress['value'] = 0
        feedback_label_var.set("No suggestions for improvement.")
        return 
    score, strength, feedback = assess_password_strength(password)
    
    strength_label_var.set(f"Strength: {strength}")
    strength_progress['value'] = score * 20
    
    feedback_text = "\n".join(feedback) if feedback else "No suggestions for improvement."
    feedback_label_var.set(feedback_text)


# Function to toggle password visibility
#Allows the user to hide or show their password, like clicking the “eye” icon on a login page.
def toggle_password():
    if password_entry.cget('show') == "*":
        password_entry.config(show="")
        eye_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        eye_button.config(text="Show")

# Function to generate a password
def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    #secrets.choice(...) randomly picks one character from the characters string.
    generated_password = ''.join(secrets.choice(characters) for _ in range(length))
    password_var.set(generated_password)
    update_feedback(None)

# Create the main application window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")

# Input box
password_var = StringVar()
password_entry = tk.Entry(root, textvariable=password_var, show="*", font=("Arial", 14))
password_entry.pack(pady=10)
password_entry.bind("<KeyRelease>", update_feedback)

# Strength label
strength_label_var = StringVar()
strength_label = tk.Label(root, textvariable=strength_label_var, font=("Arial", 12))
strength_label.pack(pady=5)

# Progress bar
strength_progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
strength_progress.pack(pady=10)

# Feedback label
feedback_label_var = StringVar()
feedback_label = tk.Label(root, textvariable=feedback_label_var, font=("Arial", 10), fg="red")
feedback_label.pack(pady=10)

# Eye button for showing/hiding the password
eye_button = tk.Button(root, text="Show", command=toggle_password, font=("Arial", 10))
eye_button.pack(pady=5)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 10))
generate_button.pack(pady=5)

# Run the application
root.mainloop()
