# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-11-01 20:01:54
# @Last Modified time: 2018-11-01 21:08:16
import argparse
import datetime
import time
from monitor import Monitor
import logging


logging.basicConfig(filename='log.txt', level=logging.INFO)


def parse_args():
    # Parses arguments

    parser = argparse.ArgumentParser(
        description="report your SS usage.")

    parser.add_argument('--test', nargs='?', default=False, type=bool,
                        help='whether to send an email immediately to test if the system works well')

    parser.add_argument('--hour', nargs='?', default=9, type=int,
                        help='the time(hour between 0 and 23) the system sent the report')

    return parser.parse_args()


def main(args):
    monitor = Monitor()

    if args.test:
        monitor.start()

    sleep_time = 30
    while True:
        now_time = datetime.datetime.now()
        if now_time.hour == args.hour and now_time.minute == 0:
            monitor.start()
            sleep_time = 60 * 60 * (24 - 1 / 60)
        else:
            if now_time.hour > args.hour:
                next_time = now_time + datetime.timedelta(days=+1)
            else:
                next_time = now_time

            next_year = next_time.date().year
            next_month = next_time.date().month
            next_day = next_time.date().day

            next_time = datetime.datetime.strptime(str(
                next_year) + "-" + str(next_month) + "-" + str(next_day) + " {}:00:00".format(args.hour), "%Y-%m-%d %H:%M:%S")

            sleep_time = int((next_time - now_time).total_seconds() * 0.9)

        logging.info('systen will sleep ' + str(sleep_time))
        time.sleep(sleep_time)


if __name__ == "__main__":
    args = parse_args()
    main(args)
