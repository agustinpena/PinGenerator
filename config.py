# configuration file; contains a bunch of
# constants needed for the script to work


# PINS PER DAY: the number of pins published daily;
# this num is used to computed when a pin can be used again
PINS_PER_DAY = 6

# default number of pins to be generated
DEFAULT_NUMBER_OF_PINS = 3

# path to folder containing all the relevant folders:
PATH_TO_GENERAL_FOLDER = '/home/joseagustin/Pictures/pins/'

# help string
HELP = '\n' \
       'Help file\n' \
       'This file creates random pins. It runs with zero or one parameter:\n' \
       '\n' \
       '     python create_pins.py        -> creates the default number of pins\n' \
       '     python create_pins.py <numb> -> creates <numb> pins\n' \
       '     python create_pins.py help   -> shows this help file\n' \
       '\n' \
       'Newly created pins will appear in the saved_pins folder.\n'
