# -*- coding: utf-8 -*-
# @Time    : 18-10-26 上午9:27
# @Author  : LogicJake
# @File    : main.py
from __future__ import print_function
from .wallpaper import start

import argparse
import getpass
import time


def parse_args():
    # Parses arguments

    parser = argparse.ArgumentParser(
        description="timely replacement wallpaper from bing.")

    parser.add_argument('--interval', nargs='?', default=3, type=float,
                        help='time interval for scripts to change wallpapers. By seconds.')

    parser.add_argument('--num', nargs='?', default=7, type=int,
                        help='number of images saved in local folder at most')

    user_name = getpass.getuser()
    wallpaper_path = '/home/' + user_name + '/wallpapers/'

    parser.add_argument('--path', nargs='?', default=wallpaper_path, type=str,
                        help='path to save images')

    return parser.parse_args()


def main():
    args = parse_args()
    wallpaper_path = args.path
    print("wallpapers are saved in " + wallpaper_path)

    while True:
        start(args)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
