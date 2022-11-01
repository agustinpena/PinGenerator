# the templates module contains functions to create individual pins

from PIL import Image as Im
import info


def generate_name(template_number, pin_number):
    if len(str(template_number)) == 1:
        template_number = '0' + str(template_number)
    today = str(info.get_date())
    return today + '_' + str(pin_number) + '_' + str(template_number) + '.png'


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
    else:
        template_number = str(template_number)
    templates_path = generic_path + 'templates' + '/'
    path_to_bg = templates_path + template_number + '_' + 'bg.png'
    path_to_fg = templates_path + template_number + '_' + 'fg.png'
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

    def f(generic_path, product_im_name, pin_number):
        bg = assemble_pin(generic_path, template_number,
                          product_im_name, x, y)
        name = generate_name(template_number, pin_number)
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

d17 = d_generic(17, 200, 110)

d18 = d_generic(18, 205, 290)

d19 = d_generic(19, 160, 250)

d20 = d_generic(20, 192, 298)

d21 = d_generic(21, 165, 300)

d22 = d_generic(22, 180, 280)

d23 = d_generic(23, 175, 290)

d24 = d_generic(24, 190, 305)

d25 = d_generic(25, 120, 220)

d26 = d_generic(26, 160, 260)

d27 = d_generic(27, 200, 300)

d28 = d_generic(28, 180, 320)

d29 = d_generic(29, 155, 185)

d30 = d_generic(30, 275, 240)

d31 = d_generic(31, 113, 253)

d32 = d_generic(32, 163, 350)

d33 = d_generic(33, 140, 310)

d34 = d_generic(34, 175, 320)

d35 = d_generic(35, 160, 220)

d36 = d_generic(36, 120, 340)

d37 = d_generic(37, 130, 350)

d38 = d_generic(38, 70, 220)

d39 = d_generic(39, 140, 240,)

d40 = d_generic(40, 103, 397)

d41 = d_generic(41, 115, 270)

d42 = d_generic(42, 40, 390)

d43 = d_generic(43, 170, 345)

d44 = d_generic(44, 150, 280)

d45 = d_generic(45, 170, 340)

d46 = d_generic(46, 90, 410)

d47 = d_generic(47, 150, 420)

d48 = d_generic(48, 170, 220)

d49 = d_generic(49, 160, 220)

d50 = d_generic(50, 205, 205)

d51 = d_generic(51, 160, 200)

d52 = d_generic(52, 165, 255)

d53 = d_generic(53, 160, 295)

d54 = d_generic(54, 200, 320)

d55 = d_generic(55, 200, 327)

d56 = d_generic(56, 170, 225)

d57 = d_generic(57, 200, 280)

d58 = d_generic(58, 160, 360)

d59 = d_generic(59, 155, 360)

d60 = d_generic(60, 160, 278)

d61 = d_generic(61, 160, 295)

d62 = d_generic(62, 159, 296)

d63 = d_generic(63, 160, 375)

d64 = d_generic(64, 100, 250)

d65 = d_generic(65, 165, 285)

d66 = d_generic(66, 245, 355)

d67 = d_generic(67, 250, 360)

d68 = d_generic(68, 160, 360)

d69 = d_generic(69, 160, 355)

d70 = d_generic(70, 310, 210)

d71 = d_generic(71, 160, 297)

d72 = d_generic(72, 265, 480)

d73 = d_generic(73, 170, 375)

d74 = d_generic(74, 142, 265)

d75 = d_generic(75, 160, 320)

d76 = d_generic(76, 170, 300)

d77 = d_generic(77, 160, 295)

d78 = d_generic(78, 160, 296)

d79 = d_generic(79, 160, 300)

d80 = d_generic(80, 160, 296)

# ADD NEW TEMPLATES BELOW ########
