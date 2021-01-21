import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import variables

mouse = MouseController()
keyboard = KeyboardController()

def doggo():
  time.sleep(0.1)
  mouse.position = variables.pets_button_position
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  time.sleep(0.1)
  mouse.position = variables.dog_position
  time.sleep(0.1)
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  keyboard.press('x')
  time.sleep(0.1)
  keyboard.release('x')
  keyboard.press('x')
  time.sleep(0.1)
  keyboard.release('x')

def foxo():
  time.sleep(0.1)
  mouse.position = variables.pets_button_position
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  time.sleep(0.1)
  mouse.position = variables.fox_position
  time.sleep(0.1)
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  keyboard.press('x')
  time.sleep(0.1)
  keyboard.release('x')
  keyboard.press('x')
  time.sleep(0.1)
  keyboard.release('x')
