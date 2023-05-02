import time
import keyboard

def auto_type():
    firstToRight = "wd"
    toRight = "wad" # Enter the message you want to auto-type here
    while True:
        keyboard.press('w')
        time.sleep(0.05)
        keyboard.press('d')
        time.sleep(0.05)
        for char in toRight:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.05) # 50ms interval between characters
            if keyboard.is_pressed('f8'):  # Check if F8 key is pressed
                return  # Exit the function if F8 key is pressed

time.sleep(10)
keyboard.add_hotkey('f7', auto_type) # Hotkey to trigger auto-typer
keyboard.wait() # Wait for hotkey
