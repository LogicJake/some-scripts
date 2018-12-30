# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-12-30 14:18:43
# @Last Modified time: 2018-12-30 15:19:28
import os
import requests
import re


class NoIPFoundException(Exception):

    def __init__(self, err='fail to find IP from the website'):
        Exception.__init__(self, err)


def get_ip():
    ip_address = 'http://59.110.167.236/ip.html'
    response = requests.get(ip_address).text

    ip = re.findall(r'\d+\.\d+\.\d+\.\d+', response)
    if len(ip) != 1:
        raise NoIPFoundException()
    return ip[0]


def ssh(ssh_command):
    index = None
    for i, part in enumerate(ssh_command):
        if '@' in part:
            index = i

    user_host = ssh_command[index]

    user, hostname = user_host.split('@')
    if hostname == 'lab':
        ip = get_ip()
        user_host = "{}@{}".format(user, ip)

    ssh_command[index] = user_host
    new_command = " ".join(ssh_command)

    convert_ssh_command = "ssh " + new_command
    os.system(convert_ssh_command)
