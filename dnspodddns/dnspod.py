#!/usr/bin/env python2
# coding:utf-8


import os
import requests
from bs4 import BeautifulSoup
import httplib

import urllib

from common import soical
from file import fileutil

ID = "55112"  # 替换成上面你创建Token时获取的ID。

Token = "ea9b6aca19586b30e1cdac44c987a37b"  # 替换成上面你创建的Token。

params = dict(

    login_token=("%s,%s" % (ID, Token)),

    format="json",

    domain_id=66031243,  # 换成你的domian_id,待会下面讲如何通过Domain.List API获取

    record_id=359045815,  # 换成你的record_id,待会下面讲如何通过Record.List API获取

    sub_domain="pi",  # 换成你上面创建的子域名

    record_line="默认",  #

)

current_ip = None

filepath = '/usr/develop/python/run/ip.txt'


def getcurrentip():
    if os.path.exists(filepath):
        return fileutil.readfirstline(filepath)
    return current_ip


def ddns(ip):
    params.update(dict(value=ip))

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}

    conn = httplib.HTTPSConnection("dnsapi.cn")

    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)

    response = conn.getresponse()

    print response.status, response.reason

    data = response.read()

    print data

    conn.close()

    return response.status == 200


# 获取外网IP
def get_out_ip(url):
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    return ip


def get_real_url(url=r'http://www.ip138.com/'):
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt, "html.parser").iframe
    return soup["src"]


if __name__ == '__main__':

    # while True:

    try:
        current_ip = getcurrentip()
        ip = get_out_ip(get_real_url())

        print ip

        if current_ip != ip:
            if ddns(ip):
                fileutil.write2file(filepath, ip)
                soical.sendMail(ip)

    except Exception as e:

        print e

        pass

    # time.sleep(30)
