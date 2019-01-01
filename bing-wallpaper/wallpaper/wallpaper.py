# -*- coding: utf-8 -*-
# @Time    : 18-10-20 下午8:42
# @Author  : LogicJake
# @File    : wallpaper.py
import getpass
import datetime
import os
from random import choice
import requests
import json
from requests import RequestException
import logging

log_file = '.wallpaper_log'
user_name = getpass.getuser()
user_path = '/home/' + user_name
log_path = os.path.join(user_path, log_file)

logging.basicConfig(filename=log_path, level=logging.INFO)


bing_wallpaper = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n={}&mkt=zh-CN'
bing_prefix = 'https://cn.bing.com'


def date_plus_day(date, day):
    date = datetime.datetime.strptime(
        date, "%Y%m%d") + datetime.timedelta(days=day)
    return date.strftime("%Y%m%d")


def download(num_saved, wallpaper_path):
    num_wallpaper = min(7, num_saved)

    try:
        content = requests.get(bing_wallpaper.format(num_wallpaper)).text
        content = json.loads(content)

        wallpapers = {}
        for i in range(num_wallpaper):
            wallpapers[date_plus_day(content['images'][i][
                                     'startdate'], 1)] = bing_prefix + content['images'][i]['url']

    except RequestException:
        logging.error('request api fail')
    except Exception as e:
        logging.error(repr(e))

    if not os.path.exists(wallpaper_path):
        os.mkdir(wallpaper_path)

    try:
        for date, url in wallpapers.items():
            save_path = wallpaper_path + date + '.jpg'
            if not os.path.exists(save_path):
                with open(save_path, 'wb') as f:
                    f.write(requests.get(url).content)
    except RequestException:
        logging.error('downloading wallpaper fail')


def set_wallpaper(wallpaper_path):
    exist_wallpapers = os.listdir(wallpaper_path)

    choose_wallpaper = choice(exist_wallpapers)
    wallpaper = wallpaper_path + choose_wallpaper

    try:
        os.system(
            'gsettings set org.gnome.desktop.background picture-uri "file:{}"'.format(wallpaper))
    except Exception:
        logging.error('setting wallpaper fail')


def check_saved_wallpaper(num_saved, wallpaper_path):
    remain_wallpapers = []

    for i in range(num_saved):
        date = (datetime.datetime.today() +
                datetime.timedelta(days=-i)).strftime("%Y%m%d")
        remain_wallpapers.append(date + '.jpg')

    exist_wallpapers = os.listdir(wallpaper_path)
    for wallpaper in exist_wallpapers:
        if wallpaper not in remain_wallpapers:
            delete_path = wallpaper_path + wallpaper
            os.remove(delete_path)


def start(args):
    wallpaper_num = args.num
    wallpaper_path = args.path

    if not wallpaper_path.endswith('/'):
        wallpaper_path += '/'

    download(wallpaper_num, wallpaper_path)
    check_saved_wallpaper(wallpaper_num, wallpaper_path)
    set_wallpaper(wallpaper_path)
