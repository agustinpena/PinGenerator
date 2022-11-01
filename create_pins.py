# main file; creates the pins for pinterest
# version 3.00

# TODO: insert sys.path line into the other modules (is it necessary?)

import sys
sys.path.insert(0, '/home/joseagustin/Pictures/pins/pintools/modules')
import templates as tmps
import info
import os
from config import DEFAULT_NUMBER_OF_PINS, PATH_TO_GENERAL_FOLDER, HELP

# number of pins to be generated
if len(sys.argv) == 2 and sys.argv[1].isnumeric():
    NUMBER_OF_PINS = int(sys.argv[1])
else:
    NUMBER_OF_PINS = DEFAULT_NUMBER_OF_PINS


# find the number of available pin templates
def find_how_many_pin_temps_there_are(generic_path):
    path = generic_path + 'templates'
    return int(len(os.listdir(path)) / 2)


# NUMBER_OF_TEMPLATES
NUMBER_OF_TEMPLATES = find_how_many_pin_temps_there_are(PATH_TO_GENERAL_FOLDER)

# template function numbers
TEMPS_FUNC_INDEXES = range(1, NUMBER_OF_TEMPLATES + 1)


def retrieve_temp_function_by_its_number(number):
    num = str(number)
    if len(num) == 1:
        num = '0' + num
    f_name = 'd' + num
    return getattr(tmps, f_name)


def generate_n_pins(generic_path, n):
    n_indexes = \
        info.select_n_random_temps_indexes_eligible_for_publication(generic_path,
                                                                    TEMPS_FUNC_INDEXES,
                                                                    n)
    n_product_imgs = \
        info.select_n_random_product_imgs_eligible_for_publication(generic_path, n)

    pin_info_f = info.generic_pin_info_funct(generic_path)

    for i in range(n):
        current_product_img_name = n_product_imgs[i]
        current_index = n_indexes[i]
        f = retrieve_temp_function_by_its_number(current_index)
        f(generic_path, current_product_img_name, i + 1)
        design_name = current_product_img_name.split('.')[0][:-3]
        pin_info_f(design_name, i + 1)

    info.write_info_to_log_pin_templates(generic_path)
    info.write_info_to_log_designs(generic_path, n_product_imgs)
    info.write_pin_info_to_publish_to_text_file(generic_path)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == 'help':
        print(HELP)
        quit()

    generate_n_pins(PATH_TO_GENERAL_FOLDER, NUMBER_OF_PINS)
    print('Successfully created ' + str(NUMBER_OF_PINS) + ' pins')


if __name__ == '__main__':
    main()
