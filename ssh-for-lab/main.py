
# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-12-30 14:18:53
# @Last Modified time: 2018-12-30 15:20:30
import sys
import myssh


def main():
    ssh_command = sys.argv[1:]
    myssh.ssh(ssh_command)


if __name__ == "__main__":
    main()
