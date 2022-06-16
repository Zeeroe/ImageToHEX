from PIL import Image
import re

file_name = 'test.png'
file_txt = re.sub(r"(\.[^.]*)$", "", file_name) + ".txt"

im = Image.open(file_name)

# get image width and height
im_w = im.size[0]
im_h = im.size[1]

print("Size: " + str(im_w) + "x" + str(im_h))


# scanning every pixel for rgb color value
rgb_list = []
for pixel_y in range(im_h):
    for pixel_x in range(im_w):
        rgb_list.append(im.getpixel((pixel_x, pixel_y)))

print("RGB: " + str(rgb_list))


# rgb to hex conversion
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


# new list of hex color values
hex_list = []
for rgb_val in rgb_list:
    hex_list.append(rgb_to_hex(rgb_val))

print("Hex: " + str(hex_list))


# splitting list by each row of pixels
final_list = []
row_start = 0  # initial start value
row_end = im_w  # initial end value
for line in range(im_h):  # num of rows/lines = height
    final_list.append(hex_list[row_start:row_end])
    row_start = row_start + im_w  # ex. 0 becomes 64, start of next row
    row_end = row_start + im_w  # ex. 64 becomes 128, end of next row

print("Final: " + str(final_list))


# write list onto file
with open(file_txt, 'w') as f:
    for line in final_list:
        for color_code in line:
            f.write(str(color_code))
            f.write(' ')  # split each code with space
        f.write('\n')  # split each line with new line
