from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup
from HTML import *
import time

# Scrape stuff p1
soup = BeautifulSoup(html, 'html.parser')

content = soup.find(class_ = 'structure-content')
lines = content.find(class_ = "screenBasic-lines")
words = lines.find_all(class_ = 'screenBasic-word')
characters = lines.find_all(class_ ="letter letter--basic screenBasic-letter")


# Keyboard and mouse control stuff
time.sleep(1)
keyboard = Controller()
a = characters[2].get_text()
print(a)

keyboard.type("O")
for x in characters:
    time.sleep(0.01)
    if x.get_text() == a:
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    else:
        keyboard.type(x.get_text())