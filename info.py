# the info module contains functions for text-processing,
# updating and reading the registy/log files

import datetime
import random
import os

templates_used = []


def register_template_number(num):
    templates_used.append(str(num))


def get_date():
    # yields date in format YYMMDD
    # TODO: check if it's a built-in feature
    # in datetime module
    data = datetime.datetime.now()
    y = str(data.year)[2:]
    m = str(data.month)
    if len(m) == 1:
        m = '0' + m
    d = str(data.day)
    if len(d) == 1:
        d = '0' + d
    return y + m + d


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


def write_info_to_registry(generic_path):
    path_to_reg = generic_path + 'registry.txt'
    joined_list = ','.join(templates_used)
    data = get_list_of_lines_from_text_file(generic_path, 'registry.txt')
    data.append(joined_list)

    if len(data) > 8:
        data = data[2:]

    write_list_to_text_file(path_to_reg, data)


def get_list_of_used_product_designs(generic_path):
    lst = []
    lines_from_log = get_list_of_lines_from_text_file(generic_path, 'log.txt')
    for line in lines_from_log:
        lst += line.split(',')
    return lst


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


def select_n_random_unused_product_imgs(generic_path, n):
    # this function differentiates designs, not just pics
    used_prod_designs = get_list_of_used_product_designs(generic_path)
    info_dict = generate_product_imgs_info_dictionary(generic_path)
    all_prod_designs = info_dict.keys()
    all_unused_designs = \
        [x for x in all_prod_designs if x not in used_prod_designs]
    n_unused_des = random.sample(all_unused_designs, n)
    n_unused_imgs = []
    for des_name in n_unused_des:
        randomly_chosen_num = random.sample(info_dict[des_name], 1)[0]
        file_name = des_name + '_' + randomly_chosen_num + '.png'
        n_unused_imgs.append(file_name)

    return n_unused_imgs


def write_info_to_log(generic_path, product_imgs_list):
    path_to_log = generic_path + 'log.txt'
    names_list = \
        [split_product_img_filename(p)[0] for p in product_imgs_list]
    line = ','.join(names_list)
    with open(path_to_log, 'a') as logfile:
        logfile.write(line + '\n')


def get_used_temps_indexes(generic_path):
    path_to_registry = generic_path + 'registry.txt'
    used_templates = []
    with open(path_to_registry, 'r') as fn:
        data = fn.readlines()
    for x in data:
        ls = x[:-1].split(',')
        for y in ls:
            if len(y) < 4:
                used_templates.append(y)
    return used_templates


def select_n_random_unused_temps_indexes(generic_path, all_funct_indexes, n):
    # modify this function when done adding templates
    # and renumbering template funcs
    used_ind = get_used_temps_indexes(generic_path)
    unused_ind = [str(x) for x in all_funct_indexes if str(x) not in used_ind]
    return random.sample(unused_ind, n)
