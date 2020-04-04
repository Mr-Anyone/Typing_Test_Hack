from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup
from  ten_html import *
import time

def press_space(keyboard):
    keyboard.press(Key.space)
    keyboard.release(Key.space)

soup = BeautifulSoup(html, 'html.parser')

content = soup.find(id = 'words')
words = content.find_all('span')

keyboard = Controller()
time.sleep(1)
for x in words:
    time.sleep(0.01)
    keyboard.type(x.get_text())
    press_space(keyboard)
