# PRODIGY_CS_04

## Simple Keylogger | Prodigy InfoTech Internship

This Python script implements a basic keylogger that records keystrokes and saves them to a log file. It utilizes the `pynput` library to monitor keyboard events.

## Usage

1. Ensure you have Python installed on your system.
    
    ```
    pip install pynput 
    ```

2. Run the script by executing the following command in your terminal:

    ```
    python Keylogger.py
    ```

3. The script will prompt you for consent to log your keystrokes. Type "yes" or "no" to indicate your consent.
4. Once consent is given, the keylogger will start recording keystrokes. Press any keys you wish to log, it will then be stored or appended to keystrokes.txt.
5. To stop the keylogger, simply close the terminal or interrupt the script.

## Functionality

- The script listens for key events using the `pynput.keyboard.Listener` class.
- When a key is pressed, it writes the corresponding character to the specified log file.
- Special keys such as space and enter are handled appropriately.
- Before starting the keylogger, the script prompts the user for consent to log keystrokes.
- The keylogger and consent prompt run on the same thread.

## Note

- This keylogger script is for educational purposes only. Do not use it for unauthorized monitoring of others' activities.
- Always respect the privacy and consent of others when developing or using software that collects personal data.

**Disclaimer:** The developer of this script is not responsible for any misuse or unethical use of the keylogger. Use it responsibly and within the boundaries of applicable laws and regulations.