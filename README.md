# PassGuard

PassGuard is a robust **Password Strength Checker and Generator** built using Python's `tkinter` library for a user-friendly graphical interface. The application evaluates the strength of a password based on various criteria and provides real-time feedback to help users create secure passwords. Additionally, it includes a secure password generator for creating strong and random passwords.

## Features

- **Password Strength Assessment**:  
  Checks password strength based on:
  - Minimum length (8+ characters).
  - Presence of uppercase and lowercase letters.
  - Inclusion of numeric and special characters.
  - Avoidance of repetitive characters.

- **Real-Time Feedback**:  
  Provides actionable suggestions for improving password strength.

- **Visual Strength Indicator**:  
  A progress bar displays the current strength of the password (Weak, Moderate, Strong, or Very Strong).

- **Password Visibility Toggle**:  
  Allows users to hide or reveal the password for convenience.

- **Password Generator**:  
  Generates random, secure passwords with customizable length.

## Technologies Used

- **Python**: Core programming language.
- **tkinter**: For creating the graphical user interface (GUI).
- **secrets**: For secure random password generation.
- **re**: For regular expressions to validate password criteria.

## How It Works

1. **Password Strength Checker**:  
   Users can enter a password, and PassGuard evaluates it in real-time, assigning a score based on defined security rules and providing a strength label (e.g., Weak, Strong).

2. **Feedback**:  
   If the password doesn't meet certain criteria, suggestions are displayed to guide the user in improving their password.

3. **Password Generator**:  
   Users can click the "Generate Password" button to create a secure, random password.

4. **Visibility Toggle**:  
   Click the "Show" button to view the password or "Hide" to mask it.

## How to Run

1. Ensure Python 3.x is installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/PassGuard.git
3. Navigate to the project directory:
   ```bash
   cd PassGuard
4. Run the script:
  ```bash
    python passguard.py

