# -*- coding: utf-8 -*-
# @Time    : 18-10-26 上午9:27
# @Author  : LogicJake
# @File    : main.py
import argparse
import getpass

import wallpaper
import time


def parse_args():
    # Parses arguments

    parser = argparse.ArgumentParser(description="timely replacement wallpaper from bing.")

    parser.add_argument('--interval', nargs='?', default=60, type=float,
                        help='time interval for scripts to change wallpapers. By minutes.')

    parser.add_argument('--num', nargs='?', default=7, type=int,
                        help='number of images saved in local folder at most')

    user_name = getpass.getuser()
    wallpaper_path = '/home/' + user_name + '/wallpapers/'

    parser.add_argument('--path', nargs='?', default=wallpaper_path, type=str,
                        help='path to save images')

    return parser.parse_args()


def main(args):
    while True:
        wallpaper.main(args)
        time.sleep(args.interval * 60)


if __name__ == "__main__":
    args = parse_args()
    main(args)
