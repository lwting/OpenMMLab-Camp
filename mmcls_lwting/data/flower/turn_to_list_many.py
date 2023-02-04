#!/usr/bin/python
# -*- coding:utf-8 -*-

import os


def generate(dir, label):
    files = os.listdir(dir)
    files.sort()
    print
    '****************'
    print
    'input :', dir
    print
    'start...'
    listText = open('val.txt', 'a')
    for file in files:
        fileType = os.path.split(file)
        if fileType[1] == '.txt':
            continue
        name = folder + '/' + file + ' ' + str(int(label)) + '\n'
        listText.write(name)
    listText.close()
    print
    'down!'
    print
    '****************'


outer_path = 'C:\\Users\\lwtin\\Desktop\\flower_dataset\\val'  # 这里是图片的目录

if __name__ == '__main__':
    i = 0
    folderlist = os.listdir(outer_path)  # 列举文件夹
    for folder in folderlist:
        generate(os.path.join(outer_path, folder), i)
        i += 1