# info module; contains functions for text-processing,
# updating and reading the log_designs/log_pin_template files

import datetime
import random
import os
from config import PINS_PER_DAY


templates_used = []


def register_template_number(num):
    templates_used.append(str(num))


def get_date():
    today = datetime.datetime.now()
    return today.strftime('%y%m%d')


pin_info_to_publish = ['Date: ' + str(get_date())]


def register_line_of_info_to_publish(line):
    pin_info_to_publish.append(line)


def get_list_of_lines_from_text_file(generic_path, text_file_name):
    path_to_file = generic_path + text_file_name
    with open(path_to_file, 'r') as text_object:
        data = text_object.readlines()
    # remove the '\n' at the end:
    return [x[:-1] for x in data]


def write_list_to_text_file(path_to_file, lst):
    with open(path_to_file, 'w') as file_write:
        for line in lst:
            file_write.write(line + '\n')


def write_info_to_log_pin_templates(generic_path):
    path_to_log = generic_path + 'log_pin_templates.txt'
    joined_list = ','.join(templates_used)
    data = get_list_of_lines_from_text_file(generic_path, 'log_pin_templates.txt')
    data.append(joined_list)
    if len(data) > 10:
        data = data[2:]
    write_list_to_text_file(path_to_log, data)


def split_product_img_filename(filename):
    a, b = filename.split('.')
    num = a[-2:]
    design_name = a[:-3]
    return design_name, num


def generate_product_imgs_info_dictionary(generic_path):
    path = generic_path + 'product_images/'
    img_dict = {}
    lst = os.listdir(path)
    for filename in lst:
        name, number = split_product_img_filename(filename)
        if name not in img_dict.keys():
            img_dict[name] = [number]
        else:
            img_dict[name].append(number)
    return img_dict


def get_items_published_in_the_last_week(generic_path, filename):
    # reads all lines in 'filename' file
    # 'log_designs.txt' -> designs, 'log_pin_templates.txt' -> pin templates
    total_list = get_list_of_lines_from_text_file(generic_path, filename)
    # extracts designs published in the last x = 6 days
    final_list = total_list[-6 * PINS_PER_DAY:]
    return final_list


def get_list_of_all_designs_eligible_for_publication(generic_path):
    # 'log_designs.txt' -> designs, 'log_pin_templates.txt' -> pin templates
    info_dict = generate_product_imgs_info_dictionary(generic_path)
    all_prod_designs = info_dict.keys()
    designs_to_exclude = \
        get_items_published_in_the_last_week(generic_path, 'log_designs.txt')
    available_designs = [x for x in all_prod_designs if x not in designs_to_exclude]
    return available_designs, info_dict


def select_n_random_product_imgs_eligible_for_publication(generic_path, n):
    # 'log_designs.txt' -> designs, 'log_pin_templates.txt' -> pin templates
    design_list, info_dict = \
        get_list_of_all_designs_eligible_for_publication(generic_path)
    list_of_n_random_eligible_designs = random.sample(design_list, n)
    # generates list of product images
    product_imgs_list = []
    for design in list_of_n_random_eligible_designs:
        str_num = random.sample(info_dict[design], 1)[0]
        image_name = design + '_' + str_num + '.jpg'
        product_imgs_list.append(image_name)
    return product_imgs_list


def write_info_to_log_designs(generic_path, product_imgs_list):
    path_to_log = generic_path + 'log_designs.txt'
    names_list = [split_product_img_filename(p)[0] for p in product_imgs_list]
    joined_list = ','.join(names_list)
    data = get_list_of_lines_from_text_file(generic_path, 'log_designs.txt')
    data.append(joined_list)
    if len(data) > 10:
        data = data[2:]
    write_list_to_text_file(path_to_log, data)


def get_list_of_pin_temps_indexes_used_in_the_last_week(generic_path):
    filename = 'log_pin_templates.txt'
    used_temp_indexes = get_items_published_in_the_last_week(generic_path, filename)
    return used_temp_indexes


def select_n_random_temps_indexes_eligible_for_publication(generic_path,
                                                           all_funct_indexes,
                                                           n):
    used_ind = get_list_of_pin_temps_indexes_used_in_the_last_week(generic_path)
    unused_ind = [str(x) for x in all_funct_indexes if str(x) not in used_ind]
    return random.sample(unused_ind, n)


def create_short_urls_dict(generic_path):
    dct = {}
    all_lines = get_list_of_lines_from_text_file(generic_path, 'urls_short.txt')
    for n in range(0, len(all_lines)-1, 2):
        dct[all_lines[n]] = all_lines[n + 1]
    return dct


def generic_pin_info_funct(generic_path):
    dct = create_short_urls_dict(generic_path)

    def f(design_name, pin_num):
        register_line_of_info_to_publish('')
        register_line_of_info_to_publish(str(pin_num))
        register_line_of_info_to_publish(design_name)
        register_line_of_info_to_publish(dct[design_name])
        register_line_of_info_to_publish('='*20)

    return f


def write_pin_info_to_publish_to_text_file(generic_path):
    file_path = generic_path + 'pin_info_to_publish.txt'
    write_list_to_text_file(file_path, pin_info_to_publish)
