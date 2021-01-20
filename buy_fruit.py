import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import variables

mouse = MouseController()
keyboard = KeyboardController()

def buy_void_apples():
  mouse.position = variables.central_position
  time.sleep(0.5)
  mouse.press(Button.left)
  time.sleep(0.5)
  mouse.release(Button.left)
  time.sleep(0.5)
  keyboard.press('7')
  time.sleep(0.5)
  keyboard.release('7')
  time.sleep(0.5)
  mouse.position = variables.buy_fruit_position
  time.sleep(0.5)
  mouse.press(Button.left)
  time.sleep(0.5)
  mouse.release(Button.left)

def buy_exotic_apples():
  mouse.position = variables.central_position
  time.sleep(0.5)
  mouse.press(Button.left)
  time.sleep(0.5)
  mouse.release(Button.left)
  time.sleep(1)
  keyboard.press('8')
  time.sleep(0.5)
  keyboard.release('8')
  time.sleep(0.5)
  mouse.scroll(0, -50)
  time.sleep(0.5)
  mouse.scroll(0, -50)
  time.sleep(0.5)
  mouse.position = variables.buy_fruit_position
  time.sleep(0.5)
  mouse.press(Button.left)
  time.sleep(0.5)
  mouse.release(Button.left)
  time.sleep(0.5)
  keyboard.press('8')
  time.sleep(0.5)
  keyboard.release('8')
