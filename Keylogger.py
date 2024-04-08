from pynput.keyboard import Key, Listener

# Path to the log file where keystrokes will be stored
log_file = "keystrokes.txt"

# Function to write the pressed key to the log file
def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(" [" + str(key) + "] ")

# Function to listen for keystrokes
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

# Function to prompt the user for consent
def prompt_permission():
    # Display the consent message box
    answer = input("This application will log your keystrokes. (YES/NO) Do you consent to this? ")
    return answer.lower() in ["yes", "y"]

# Function to handle keylogger and GUI on the same thread
def main():
    if prompt_permission():
        print("\nEnter input: ")
        start_keylogger()
    else:
        print("User denied permission.")


# Main function
if __name__ == "__main__":
    main()
