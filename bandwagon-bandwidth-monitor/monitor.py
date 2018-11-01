# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-10-31 19:54:21
# @Last Modified time: 2018-11-01 21:07:11

import requests
from lxml import etree
import json
from json import JSONDecodeError
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import logging

mail_host = 'smtp.qq.com'
logging.basicConfig(filename='log.txt', level=logging.INFO)


class Monitor(object):

    def __init__(self):
        super(Monitor, self).__init__()
        file_name = 'config.json'
        try:
            with open(file_name, 'r') as f:
                config = json.load(f)
            self.login_ip = config['login']['ip']
            self.login_password = config['login']['password']
            self.mail_address = config['mail']['address']
            self.mail_password = config['mail']['password']
        except JSONDecodeError as e:
            logging.error('JSONDecodeError: ' + str(e))
        except KeyError as e:
            logging.error("KeyError: no key " + str(e))

    def login(self):
        login_url = 'https://kiwivm.64clouds.com/?mode=login'
        s = requests.Session()

        try:
            request = s.post(
                login_url, data={'login': self.login_ip, 'password': self.login_password})
            logging.info('login succeed')
        except Exception:
            logging.error('Login fail!')
            exit(-1)

        content = request.text

        if 'Using secure connection' in content:
            logging.error('Login incorrect')
            exit(-1)
        else:
            self.session = s

    def get_info(self):
        info_url = 'https://kiwivm.64clouds.com/kiwi-main-controls.php'
        content = self.session.get(info_url).text
        html = etree.HTML(content)

        reset = html.xpath('//font')[3].text.split(':')[1].strip()
        usage = html.xpath('//font')[4].text

        self.reset_date = reset
        self.usage = usage.split('/')[0]
        self.total = usage.split('/')[1].split(' ')[0]
        self.date = time.strftime("%Y-%m-%d", time.localtime())
        self.average_usage = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())

        start_date = time.mktime(time.strptime(self.date, '%Y-%m-%d'))
        end_date = time.mktime(time.strptime(self.reset_date, '%Y-%m-%d'))
        remaining_days = int((end_date - start_date) / (24 * 60 * 60))
        self.average_usage = round((float(self.total) -
                                    float(self.usage)) / remaining_days, 2)

    def send_email(self):
        with open('content.html', 'r') as f:
            content = f.read()
        attr = self.__dict__

        message = MIMEText(content.format(**attr), 'html', 'utf-8')
        message['From'] = Header("bandwagon ss monitor", 'utf-8')   # 发送者
        message['To'] = Header("admin", 'utf-8')        # 接收者

        subject = 'SS Usage Report'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)
            smtpObj.login(self.mail_address, self.mail_password)
            smtpObj.sendmail(self.mail_address,
                             self.mail_address, message.as_string())
            logging.info('send report')
        except smtplib.SMTPException as e:
            logging.error('SMTPException' + str(e))

    def start(self):
        self.login()
        self.get_info()
        self.send_email()


if __name__ == '__main__':
    monitor = Monitor()
    monitor.start()
