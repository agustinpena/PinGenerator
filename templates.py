# the templates module contains functions to create individual pins

from PIL import Image as Im
import info


def generate_name(template_number):
    if len(str(template_number)) == 1:
        template_number = '0' + str(template_number)
    return info.get_date() + '_' + str(template_number) + '.png'


def save_image_and_update_templates_used(generic_path,
                                         pil_object,
                                         template_number,
                                         new_img_name):
    path_to_new_file = generic_path + 'saved_pins/' + new_img_name
    pil_object.save(path_to_new_file)
    info.register_template_number(template_number)


def find_all_paths(generic_path, template_number, product_img_name):
    if len(str(template_number)) == 1:
        template_number = '0' + str(template_number)
    path = generic_path + 'template_' + str(template_number) + '/'
    path_to_bg = path + 'bg.png'
    path_to_fg = path + 'fg.png'
    path_to_pr = generic_path + 'product_images/' + product_img_name
    return path_to_bg, path_to_pr, path_to_fg


def open_all_img_files(path_to_bg, path_to_prod, path_to_fg):
    b = Im.open(path_to_bg)
    p = Im.open(path_to_prod).convert('RGBA')
    f = Im.open(path_to_fg).convert('RGBA')
    return b, p, f


def assemble_pin(generic_path, template_number, product_image_name, x, y):

    path_to_bg, path_to_pr, path_to_fg = find_all_paths(generic_path,
                                                        template_number,
                                                        product_image_name)
    backg, product, foreg = open_all_img_files(path_to_bg, path_to_pr, path_to_fg)
    backg.paste(product, (x, y), product)
    backg.paste(foreg, (0, 0), foreg)
    return backg


def d_generic(template_number, x, y):

    def f(generic_path, product_im_name):
        bg = assemble_pin(generic_path, template_number,
                          product_im_name, x, y)
        name = generate_name(template_number)
        save_image_and_update_templates_used(generic_path, bg,
                                             template_number, name)

    return f


d01 = d_generic(1, 160, 290)

d02 = d_generic(2, 200, 480)

d03 = d_generic(3, 210, 90)

d04 = d_generic(4, 165, 270)

d05 = d_generic(5, 160, 250)

d06 = d_generic(6, 265, 330)

d07 = d_generic(7, 110, 500)

d08 = d_generic(8, 100, 140)

d09 = d_generic(9, 210, 240)

d10 = d_generic(10, 100, 85)

d11 = d_generic(11, 160, 420)

d12 = d_generic(12, 180, 300)

d13 = d_generic(13, 171, 190)

d14 = d_generic(14, 150, 320)

d15 = d_generic(15, 60, 375)

d16 = d_generic(16, 160, 370)

d17 = d_generic(17, 190, 115)

d18 = d_generic(18, 205, 290)

d19 = d_generic(19, 160, 250)

d20 = d_generic(20, 192, 298)

d21 = d_generic(21, 165, 300)

d22 = d_generic(22, 180, 280)

d23 = d_generic(23, 175, 290)

d24 = d_generic(24, 190, 305)
