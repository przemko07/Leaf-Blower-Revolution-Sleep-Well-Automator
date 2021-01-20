from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from prestige import prestige
from areas import to_the_void, to_the_abyss
from buy_fruit import buy_exotic_apples, buy_void_apples

import time
mouse = MouseController()
keyboard = KeyboardController()

#print('The current pointer position is {0}'.format(mouse.position))
x = 0
while(True):
  print(f"This is the prestige number {(x/60) +1} in the cycle. Please don't move the mouse for now.")
  prestige()
  print("You now have 20 seconds to stop the program if you want to.")
  time.sleep(20)
  print("Time's up, don't move the mouse untill further notice.")
  to_the_void()
  time.sleep(2)
  buy_void_apples()
  time.sleep(2)
  to_the_abyss()
  time.sleep(6)
  buy_exotic_apples()
  print(f"You now have {(x/60) +1} minute(s) to stop the program if you want to.")
  time.sleep(60 +x)
  x += 60
