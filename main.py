from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from prestige import prestige, crunch, exotic_BLC
from areas import to_the_void, to_the_abyss
from buy_fruit import buy_exotic_apples, buy_void_apples
from blower import blower
from pets import doggo, foxo

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
  time.sleep(10)
  buy_exotic_apples()
  #print(f"You now have {(x/60) +1} minute(s) to stop the program if you want to.")
  start_time = time.time()
  while(time.time() - start_time < 60 +x):
    blower()
    time.sleep(5)
  #time.sleep(60 +x)
  x += 60
  if x/60 > -1:
    time.sleep(1)
    foxo()
    time.sleep(1)
    crunch()
    time.sleep(20)
    doggo()
    time.sleep(20)
    x = 0

