# -*- coding: utf-8 -*-
# @Time    : 18-10-20 下午8:42
# @Author  : LogicJake
# @File    : wallpaper.py
import datetime
import os
from json import JSONDecodeError

import requests
import json

from requests import RequestException

bing_wallpaper = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
bing_prefix = 'https://cn.bing.com'

dir = 'wallpapers'

pwd = os.path.dirname(os.path.abspath(__file__))


def download():
    wallpaper_path = pwd + os.path.sep + dir + os.path.sep
    print(wallpaper_path)
    try:
        content = requests.get(bing_wallpaper).text
        content = json.loads(content)
        wallpaper = bing_prefix + content['images'][0]['url']
    except RequestException:
        print('ERROR: request api fail')
    except JSONDecodeError:
        print('ERROR: api content error')

    if not os.path.exists(wallpaper_path):
        print('make directory: {}'.format(dir))
        os.mkdir(wallpaper_path)

    try:
        print('downloading wallpaper')
        with open(wallpaper_path + datetime.date.today().strftime("%Y%m%d") + '.jpg', 'wb') as f:
            f.write(requests.get(wallpaper).content)
    except RequestException:
        print('ERROR: downloading wallpaper fail')


def set_wallpaper():
    wallpaper = pwd + os.path.sep + dir + os.path.sep + datetime.date.today().strftime("%Y%m%d") + '.jpg'

    if not os.path.exists(wallpaper):
        download()

    try:
        print('setting wallpaper')
        os.system('gsettings set org.gnome.desktop.background picture-uri "file:{}"'.format(wallpaper))
    except Exception:
        print('ERROR: setting wallpaper fail')


set_wallpaper()
