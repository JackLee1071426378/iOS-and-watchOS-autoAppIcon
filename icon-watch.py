#!/usr/bin/env python
# coding: utf-8

import sys
import os

try:
    from PIL import Image
except:
    print ('\033[31m' + '缺少Image模块，正在安装Image模块，请等待...' + '\033[0m')
    success = os.system('python -m pip install Image')
    if success == 0:
      print('\033[7;32m' + 'Image模块安装成功.' + '\033[0m')
      from PIL import Image
    else:
      print ('\033[31m' + 'Image安装失败，请手动在终端执行：\'python -m pip install Image\'重新安装.' + '\033[0m')
      quit()

outPutPath = os.path.expanduser('~') + '/Desktop/AppIcon/'

if not os.path.exists(outPutPath):
    os.mkdir(outPutPath)

if len(sys.argv) <= 1:
    print ('\033[31m' + '请输入图片路径,eg: python autoExportAppIcon.py /path/xxx.png' + '\033[0m')
    quit()

ImageName = sys.argv[1]
# print('图片名字为：' + ImageName)
originImg = ''
try:
    originImg = Image.open(ImageName)
except:
    print ('\033[31m' + '\'' + ImageName + '\'' + '，该文件不是图片文件，请检查文件路径.' + '\033[0m')
    quit()

# 24x24
# img0 = originImg.resize((24,24), Image.ANTIALIAS)
img1 = originImg.resize((48,48), Image.ANTIALIAS)
# img0.save(outPutPath + 'appIcon24x24.png',"png")
img1.save(outPutPath + 'appIcon24x24@2x.png',"png")

# 27.5x27.5
# img2 = originImg.resize((27.5,27.5), Image.ANTIALIAS)
img3 = originImg.resize((55,55), Image.ANTIALIAS)
# img2.save(outPutPath + 'appIcon27.5x27.5.png',"png")
img3.save(outPutPath + 'appIcon27.5x27.5@2x.png',"png")

# 29x29
# img4 = originImg.resize((29,29), Image.ANTIALIAS)
img5 = originImg.resize((58,58), Image.ANTIALIAS)
img6 = originImg.resize((87,87), Image.ANTIALIAS)
# img4.save(outPutPath + 'appIcon29x29.png',"png")
img5.save(outPutPath + 'appIcon29x29@2x.png',"png")
img6.save(outPutPath + 'appIcon29x29@3x.png',"png")

# 40x40
# img7 = originImg.resize((40,40), Image.ANTIALIAS)
img8 = originImg.resize((80,80), Image.ANTIALIAS)
# img7.save(outPutPath + 'appIcon40x40.png',"png")
img8.save(outPutPath + 'appIcon40x40@2x.png',"png")

# 44x44
# img9 = originImg.resize((44,44), Image.ANTIALIAS)
img10 = originImg.resize((88,88), Image.ANTIALIAS)
# img9.save(outPutPath + 'appIcon44x44.png',"png")
img10.save(outPutPath + 'appIcon44x44@2x.png',"png")

# 50x50
# img11 = originImg.resize((50,50), Image.ANTIALIAS)
img12 = originImg.resize((100,100), Image.ANTIALIAS)
# img11.save(outPutPath + 'appIcon50x50.png',"png")
img12.save(outPutPath + 'appIcon50x50@2x.png',"png")

# 86x86
# img13 = originImg.resize((86,86), Image.ANTIALIAS)
img14 = originImg.resize((172,172), Image.ANTIALIAS)
# img13.save(outPutPath + 'appIcon86x86.png',"png")
img14.save(outPutPath + 'appIcon86x86@2x.png',"png")

# 98x98
# img15 = originImg.resize((98,98), Image.ANTIALIAS)
img16 = originImg.resize((196,196), Image.ANTIALIAS)
# img15.save(outPutPath + 'appIcon98x98.png',"png")
img16.save(outPutPath + 'appIcon98x98@2x.png',"png")

# 108x108
# img17 = originImg.resize((108,108), Image.ANTIALIAS)
img18 = originImg.resize((216,216), Image.ANTIALIAS)
# img17.save(outPutPath + 'appIcon108x108.png',"png")
img18.save(outPutPath + 'appIcon108x108@2x.png',"png")

# Market
originImg.save(outPutPath + 'appIconMarket.png',"png")

# 创建Contents.json文件

content = '''
{
    "images" : [
    {
        "size" : "24x24",
        "idiom" : "watch",
        "filename" : "appIcon24x24@2x.png",
        "scale" : "2x",
        "role" : "notificationCenter",
        "subtype" : "38mm"
    },
    {
        "size" : "27.5x27.5",
        "idiom" : "watch",
        "filename" : "appIcon27.5x27.5@2x.png",
        "scale" : "2x",
        "role" : "notificationCenter",
        "subtype" : "42mm"
    },
    {
        "size" : "29x29",
        "idiom" : "watch",
        "filename" : "appIcon29x29@2x.png",
        "role" : "companionSettings",
        "scale" : "2x"
    },
    {
        "size" : "29x29",
        "idiom" : "watch",
        "filename" : "appIcon29x29@3x.png",
        "role" : "companionSettings",
        "scale" : "3x"
    },
    {
        "size" : "40x40",
        "idiom" : "watch",
        "filename" : "appIcon40x40@2x.png",
        "scale" : "2x",
        "role" : "appLauncher",
        "subtype" : "38mm"
    },
    {
        "size" : "44x44",
        "idiom" : "watch",
        "filename" : "appIcon44x44@2x.png",
        "scale" : "2x",
        "role" : "appLauncher",
        "subtype" : "40mm"
    },
    {
        "size" : "50x50",
        "idiom" : "watch",
        "filename" : "appIcon50x50@2x.png",
        "scale" : "2x",
        "role" : "appLauncher",
        "subtype" : "44mm"
    },
    {
        "size" : "86x86",
        "idiom" : "watch",
        "filename" : "appIcon86x86@2x.png",
        "scale" : "2x",
        "role" : "quickLook",
        "subtype" : "38mm"
    },
    {
        "size" : "98x98",
        "idiom" : "watch",
        "filename" : "appIcon98x98@2x.png",
        "scale" : "2x",
        "role" : "quickLook",
        "subtype" : "42mm"
    },
    {
        "size" : "108x108",
        "idiom" : "watch",
        "filename" : "appIcon108x108@2x.png",
        "scale" : "2x",
        "role" : "quickLook",
        "subtype" : "44mm"
    },
    {
        "idiom" : "watch-marketing",
        "filename" : "appIconMarket.png",
        "size" : "1024x1024",
        "scale" : "1x"
    }
    ],
    "info" : {
        "version" : 1,
        "author" : "xcode"
    }
}
'''
f = open(outPutPath + 'Contents.json', 'w')
f.write(content)

print('\033[7;32m' + '文件输出文件夹：' + outPutPath + '\033[0m')
os.system('open ' + outPutPath)
