# -*- coding: utf-8 -*-
# @Time    : 18-10-26 上午9:27
# @Author  : LogicJake
# @File    : main.py
from __future__ import print_function
from .wallpaper import start

import atexit
import argparse
import getpass
import time
import os
import sys
import signal

pid_file = '.wallpaper_pid'
user_name = getpass.getuser()
user_path = '/home/' + user_name
pid_path = os.path.join(user_path, pid_file)


def parse_args():
    # Parses arguments

    parser = argparse.ArgumentParser(
        description="timely replacement wallpaper from bing.")

    parser.add_argument('stop', nargs='?', default='run', type=str,
                        help='stop wallpaper')

    parser.add_argument('--interval', nargs='?', default=3, type=float,
                        help='time interval for scripts to change wallpapers. By seconds.')

    parser.add_argument('--num', nargs='?', default=7, type=int,
                        help='number of images saved in local folder at most')

    wallpaper_path = '/home/' + user_name + '/.wallpapers/'

    parser.add_argument('--path', nargs='?', default=wallpaper_path, type=str,
                        help='path to save images')

    return parser.parse_args()


def startByDeamon(args):
    pid = os.fork()
    if pid:
        sys.exit(0)

    os.chdir('/')
    os.umask(0)
    os.setsid()

    _pid = os.fork()
    if _pid:
        sys.exit(0)

    sys.stdout.flush()
    sys.stderr.flush()

    with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
        os.dup2(read_null.fileno(), sys.stdin.fileno())
        os.dup2(write_null.fileno(), sys.stdout.fileno())
        os.dup2(write_null.fileno(), sys.stderr.fileno())

    with open(pid_path, 'w+') as f:
        f.write(str(os.getpid()))
        atexit.register(os.remove, pid_file)

    while True:
        start(args)
        time.sleep(args.interval)


def stopDeamon():
    try:
        with open(pid_path, 'r') as f:
            pid = f.readline()
            try:
                os.kill(int(pid), signal.SIGKILL)
            except ProcessLookupError:
                pass
        os.remove(pid_path)
    except IOError:
        pass


def main():
    args = parse_args()
    if args.stop == 'stop':
        stopDeamon()
    elif args.stop == 'run':
        # try to delete
        stopDeamon()
        wallpaper_path = args.path
        print("wallpapers are saved in " + wallpaper_path)
        startByDeamon(args)
    else:
        print('invalid argument')


if __name__ == "__main__":
    main()
