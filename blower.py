import time
from pynput.mouse import Button, Controller as MouseController
import variables

mouse = MouseController()

def blower():
  iterations = 0
  while iterations < 5:
    for y_value in range(variables.min_height_position, variables.max_height_position, 50):
      for x_value in range(variables.min_width_position,variables.max_width_position, 200):
        mouse.position = (x_value, y_value)
        time.sleep(0.1)

    iterations += 1
