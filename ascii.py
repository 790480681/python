# -*- coding=utf-8 -*-

from PIL import Image#PIL库导入Image模块
import argparse#导入argparse，argparse 库是用来管理命令行参数输入的
# argparse 处理命令行参数，目标是获取输入的图片路径、输出字符画的宽和高以及输出文件的路径：
#构造ArgumentParser实例
parser = argparse.ArgumentParser()

#定义file、output、width、height
parser.add_argument('file')     #
parser.add_argument('-o', '--output')   #????
parser.add_argument('--width', type = int, default = 60) #??????
parser.add_argument('--height', type = int, default = 60) #??????

#????
args = parser.parse_args()
#解析获取参数
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*abcdoahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# ?256?????70????
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    #????????
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
