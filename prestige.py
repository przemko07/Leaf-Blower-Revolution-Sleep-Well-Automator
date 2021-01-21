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

def crunch():
  time.sleep(0.1)
  mouse.position = variables.central_position
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  time.sleep(0.1)
  keyboard.press('c')
  time.sleep(0.5)
  keyboard.release('c')
  time.sleep(1)
  mouse.position = variables.prestige_button_position
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  mouse.position = variables.confirm_button_position
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)

def exotic_BLC():
  time.sleep(0.1)
  mouse.position = variables.central_position
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  time.sleep(1)
  keyboard.press('8')
  time.sleep(0.5)
  keyboard.release('8')
  time.sleep(0.1)
  mouse.position = variables.exotic_BLC_plus_max
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  time.sleep(0.1)
  mouse.position = variables.exotic_moar_BLC_max
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
