import time
from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()

# There are two ways you can configure this numbers: you adjust the position of your mouse and run
# the program or you uncomment the for loop in this file and run it following the instructions.
#  You can memorize the points using this image https://ibb.co/qmp58QH. After this, copy the variables to the
# variables.py file.


#print('The current pointer position is {0}'.format(mouse.position))


list_of_variables = ["prestige_button_position", "confirm_button_position", "central_position",\
                    "void_button_position", "abyss_button_position", "buy_fruit_position", \
                    "max_height_position", "min_height_position" ,"max_width_position", "min_width_position",
                    "pets_button_position", "bunny_position", "cat_position", "deer_position", "dog_position",
                    "fox_position", "monkey_position", "exotic_BLC_plus_max ","exotic_moar_BLC_max" ]

for position in range(15,len(list_of_variables)):
  print(f"You have 5 seconds to move to {list_of_variables[position]} ")
  time.sleep(5)
  print(f"{list_of_variables[position]} = {mouse.position}")


