from PIL import Image
import sys
import os
from os.path import join

os.system("touch labels.csv")

with open('labels.csv') as f:
    contents = [row.split('\t') for row in f.read().split('\n')]

already_labelled = [row[0] for row in contents]

# print(already_labelled)

folder_name = sys.argv[1]

file_num = len([name for name in os.listdir(folder_name)])
print (file_num)


images = []
for root, dirs, files in os.walk(folder_name):
    images += files

images = [join(folder_name, img) for img in images if img not in already_labelled]

count = 1
for im_name in images:
    im_basic_name = 'none'
    #im = Image.open(im_name)
    #im.show()
    label = raw_input("Image: " + im_basic_name + ", " + str(count) + " of " + str(file_num) + ":")
    count += 1
    #im.close()
    with open('labels.csv', 'a+') as f:
       f.write(im_basic_name + '\t' + label + '\n')
    #os.system("killall display")
