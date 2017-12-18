import pyautogui
from pynput import keyboard

#on press events here
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

#on release events here
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key == keyboard.Key.space:
        pyautogui.typewrite(['backspace'])
        pyautogui.typewrite(':clap:')


#listening for individual keystrokes
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    #activating listener
    listener.join()