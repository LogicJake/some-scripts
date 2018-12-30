
# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-12-30 14:18:53
# @Last Modified time: 2018-12-30 18:28:44
import sys
from .myssh import ssh


def main():
    ssh_command = sys.argv[1:]
    ssh(ssh_command)


if __name__ == "__main__":
    main()
