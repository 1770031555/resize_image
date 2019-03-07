# coding=utf-8
# 把这个文件放到和  './cat' & "./dog" 同一级的目录之下

import os
from PIL import Image
import sys
# -START------------- YOU SHOULD CHANGE THE TWO PARAMETERS
_RESIZE_IMAGE_HEIGHT = 1280
_RESIZE_IMAGE_WIDTH = 720
# -END----------------------------------------------------

def find_all_image(directory="./"):
    """
    找到该目录下所有的文件，这个仅针对于当前的目录结构，更加鲁棒性的代码还没想到
    :param directory:
    :return:
    """
    image_file_list = list()
    folder_list = [os.path.abspath(path=path) for path in os.walk(directory).__next__()[1]]
    for folder in folder_list:
        for file in os.listdir(folder):
            # image_file_list.append(folder + file)
            image_file_list.append(str(folder)+"\\"+str(file))
    print(image_file_list)
    return image_file_list


def resize_image(image_files_list):
    """
    这个是主函数，将对应地址的image转换image后重新存入
    :param filename_list: should be a list
    :return:
    """
    for image in image_files_list:
        img = Image.open(image)
        img = img.resize((_RESIZE_IMAGE_WIDTH, _RESIZE_IMAGE_HEIGHT), Image.ANTIALIAS)
        # MARK 这里img.resize时候 img.resize(( WHAT_YOU_NEED_WIDTH, WHAT_YOU_NEED_HEIGHT))
        print("转换图像{}，变为高：{}；宽：{}".format(image, img.height, img.width))
        img.save(image)
    print("所有图像resize完成")

def main():
    image_files_list = find_all_image()
    resize_image(image_files_list=image_files_list)


if __name__ == '__main__':
    main()





