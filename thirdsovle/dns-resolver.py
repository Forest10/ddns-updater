#!/usr/bin/python3
# -*- coding:UTF-8 -*-


import dns.resolver

import httplib2

iplist = []
# appdomain = '.xn--zfr164b'
appdomain = 'www.baidu.com'


def get_iplist(domain):
    try:
        A = dns.resolver.query(domain, 'A')
        print(A)
    except Exception as e:
        print("dns resolver error %s" % str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True


def checkip(ip):
    # for ip in iplist:
    checkurl = ip + ":80"
    getcontent = ""
    httplib2.socket.setdefaulttimeout(5)
    # conn = httplib2.HTTPConnection(checkurl) #httplib和httplib2的区别
    conn = httplib2.Http()
    try:
        # conn.request("GET","/",header = {"Host":appdomain})
        resp, getcontent = conn.request("http://" + checkurl)
        # print("resp is %s" % resp)
        # getcontent = resp.read(15)
    finally:
        # if getcontent == "<!doctype html>":#httplib2和httplib的区别
        if resp['status'] == '200':
            print("%s is OK!" % ip)
        else:
            print("%s is ERROR!" % ip)


if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error.")
