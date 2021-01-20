import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import variables

mouse = MouseController()
keyboard = KeyboardController()


def to_the_void():
  time.sleep(0.5)
  mouse.position  = variables.central_position
  time.sleep(0.5)
  mouse.press(Button.left)
  time.sleep(0.5)
  mouse.release(Button.left)
  time.sleep(0.5)
  keyboard.press('v')
  time.sleep(0.5)
  keyboard.release('v')
  time.sleep(0.5)
  mouse.position = variables.void_button_position
  time.sleep(0.5)
  mouse.press(Button.left)
  time.sleep(0.5)
  mouse.release(Button.left)

def to_the_abyss():
  time.sleep(0.5)
  mouse.position = variables.central_position
  time.sleep(0.5)
  mouse.press(Button.left)
  time.sleep(0.5)
  mouse.release(Button.left)
  time.sleep(0.5)
  keyboard.press('v')
  time.sleep(0.5)
  keyboard.release('v')
  time.sleep(0.5)
  mouse.position = variables.abyss_button_position
  time.sleep(0.5)
  mouse.press(Button.left)
  time.sleep(0.5)
  mouse.release(Button.left)
