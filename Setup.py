# coding=utf-8

import os
os.system('pip install pipreqs')
# --force 覆盖原有的 requirements.txt 清单文件
os.system('pipreqs --force ./')
# -r 根据 requirements.txt 文件安装依赖
os.system('pip install -r requirements.txt')
