import time
from pynput.keyboard import Listener, Key
from pynput.mouse import Controller as Mouse, Button

# Random Variable
run = True
click = False
times = 10
count = 0
mouse = Mouse()

# This would be some random variable for the program
def on_press(key):
    pass

def on_release(key):
    global run, click
    if run:
        if key == Key.space and not click:
            click = True
        elif key == Key.space and click:
            click = False

        if key == Key.backspace:
            run = False


listener = Listener(on_press, on_release)
listener.start()

# This is the main clicktest
while run:
    if click:
        time.sleep(0.1)
        mouse.click(Button.left, times)
        count += 1
listener.stop()
print(f'You have click {count * times} time from start to end!')
