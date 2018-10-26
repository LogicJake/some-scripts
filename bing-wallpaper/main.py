# -*- coding: utf-8 -*-
# @Time    : 18-10-26 上午9:27
# @Author  : LogicJake
# @File    : main.py
import argparse
import getpass

import wallpaper
import threading as thd
import time


def parse_args():
    # Parses arguments

    parser = argparse.ArgumentParser(description="timely replacement wallpaper from bing.")

    parser.add_argument('--interval', nargs='?', default=1, type=int,
                        help='the interval between wallpaper replacement. By hours')

    parser.add_argument('--num', nargs='?', default=7, type=int,
                        help='the maximum value of saved wallpaper')

    user_name = getpass.getuser()
    wallpaper_path = '/home/' + user_name + '/wallpapers/'

    parser.add_argument('--path', nargs='?', default=wallpaper_path, type=str,
                        help='the path to save wallpaper')

    return parser.parse_args()


def main(args):
    while True:
        wallpaper.main(args)
        time.sleep(args.interval * 60 * 60)


if __name__ == "__main__":
    args = parse_args()
    main(args)
