# main file; creates the pins for pinterest

import templates as tmps
import info

# number of pins to be generated
NUMBER_OF_PINS = 3

# path to folder containing all the template folders:
PATH_TO_GENERAL_FOLDER = '/home/joseagustin/Pictures/pinterest/'

# template function numbers
TEMPS_FUNC_INDEXES = [n for n in range(1, 25)]


def retrieve_temp_function_by_its_number(number):
    num = str(number)
    if len(num) == 1:
        num = '0' + num
    f_name = 'd' + num
    return getattr(tmps, f_name)


def generate_n_pins(generic_path, n):
    n_indexes = info.select_n_random_unused_temps_indexes(generic_path,
                                                          TEMPS_FUNC_INDEXES,
                                                          n)
    n_product_imgs = info.select_n_random_unused_product_imgs(generic_path, n)

    for i in range(n):
        current_product_img_name = n_product_imgs[i]
        current_index = n_indexes[i]
        f = retrieve_temp_function_by_its_number(current_index)
        f(generic_path, current_product_img_name)

    info.write_info_to_registry(generic_path)
    info.write_info_to_log(generic_path, n_product_imgs)


def main():
    # tmps.d16(PATH_TO_GENERAL_FOLDER, 'product.png')
    generate_n_pins(PATH_TO_GENERAL_FOLDER, NUMBER_OF_PINS)
    print()
    print('Successfully created ' + str(NUMBER_OF_PINS) + ' pins!')


if __name__ == '__main__':
    main()
