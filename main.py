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
  print("Time's up, don't move the mouse until further notice.")
  to_the_void()
  time.sleep(2)
  buy_void_apples()
  time.sleep(2)
  to_the_abyss()
  time.sleep(10)
  buy_exotic_apples()
  #print(f"You now have {(x/60) +1} minute(s) to stop the program if you want to.")
  start_time = time.time()
  lawn_blown = 0
  print("Now preparing to blow the lawn.")
  while(time.time() - start_time < 60 +x):
    lawn_blown += 1
    print(f"Don't move the mouse until further notice. Lawn blown {lawn_blown} of {((x + 60) / 30)+1}.")
    blower()
    print(f"You now have 5 seconds to finish the program (if you want to).")
    time.sleep(5)
  #time.sleep(60 +x)
  x += 60
  if x/60 > 10:
    print("Preparing to crunch! It will take aroung a minute.")
    time.sleep(1)
    foxo()
    time.sleep(1)
    crunch()
    time.sleep(20)
    doggo()
    time.sleep(20)
    x = 0

