#!/usr/bin/env python2
# -*- coding: utf-8 -*-


# 解决'ascii' codec can't decode byte 0xe5 in position 26: ordinal not in range(128)
import sys

reload(sys)
sys.setdefaultencoding('utf8')
# 解决'ascii' codec can't decode byte 0xe5 in position 26: ordinal not in range(128)
import json
import requests
from bs4 import BeautifulSoup
from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109 import (AddDomainRecordRequest, DescribeDomainRecordsRequest,
                                               UpdateDomainRecordRequest)
import mailsender;


# 获取配置
def get_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config


# 从域名中获取RR和主域名
def get_domain_parts(domain):
    parts = domain.split('.')
    length = len(parts)
    if length > 2:
        return '.'.join(parts[0:length - 2]), '.'.join(parts[length - 2:length])
    else:
        return '@', '.'.join(parts[0:length])


# 获取解析记录
def get_record(acs_client, domain_name, rr):
    request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    request.set_DomainName(domain_name)
    request.set_accept_format('json')
    records = json.JSONDecoder().decode(acs_client.do_action_with_exception(request).decode())['DomainRecords'][
        'Record']
    for record in records:
        if record['RR'] == rr:
            return record['RecordId'], record['Value']
    return None, None


# 添加记录
def add_record(acs_client, rr, domain_name, current_ip, ttl):
    request = AddDomainRecordRequest.AddDomainRecordRequest()
    request.set_RR(rr)
    request.set_Type('A')
    request.set_DomainName(domain_name)
    request.set_Value(current_ip)
    request.set_TTL(ttl)
    request.set_accept_format('json')
    result = acs_client.do_action_with_exception(request)
    return result


# 更新记录
def update_record(acs_client, record_id, rr, current_ip, ttl):
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    request.set_RR(rr)
    request.set_Type('A')
    request.set_Value(current_ip)
    request.set_RecordId(record_id)
    request.set_TTL(ttl)
    request.set_accept_format('json')
    result = acs_client.do_action_with_exception(request)
    return result


# 拿到路由器外网IP
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


# 主函数
def main():
    config = get_config()
    acs_client = client.AcsClient(config['access_key_id'], config['access_key_secret'], config['region_id'])
    try:
        current_ip = get_out_ip(get_real_url())
        mailsender.sendMail("单纯运行获取到树莓派IP:" + current_ip)
        for domain in config['domains']:
            rr, domain_name = get_domain_parts(domain)
            record_id, record_ip = get_record(acs_client, domain_name, rr)
            if record_id is None:
                add_record(acs_client, rr, domain_name, current_ip, config['ttl'])
            else:
                if record_ip != current_ip:
                    update_record(acs_client, record_id, rr, current_ip, config['ttl'])
                    mailsender.sendMail(current_ip)
    except Exception as e:
        mailsender.sendMail(e)
        raise


if __name__ == '__main__':
    main()
