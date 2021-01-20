import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import variables

mouse = MouseController()
keyboard = KeyboardController()

def prestige():
  time.sleep(0.1)
  mouse.position  = variables.central_position
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  time.sleep(0.1)
  keyboard.press('x')
  time.sleep(0.5)
  keyboard.release('x')
  time.sleep(1)
  mouse.position = variables.prestige_button_position
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  mouse.position = variables.confirm_button_position
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
