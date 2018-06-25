# 自动更新DNS解析（阿里云解析）

## 准备工作

1. 配置好config.json中的`access_key_id`和`access_key_secret`，可以在阿里云中找到，在`domains`中配置好需要批量更新解析的域名

## 树莓派 Linux服务器

1. 安装python
2. 安装第三方库

    ```
    pip install aliyun-python-sdk-core
    pip install aliyun-python-sdk-alidns
    ```

3. 配置crontab定时脚本
*/30  *       *          *     * python /usr/develop/python/run/ddns.py >> /home/pi/ddns/ddns.log 2>&1





## 外网IP获取方式

目前使用[http://v4.ipv6-test.com/api/myip.php](http://v4.ipv6-test.com/api/myip.php)来获取IP地址，未来如果失效，可以采用如下其他几种获取方式：

* POST: [http://ip.taobao.com/service/getIpInfo.php?ip=myip](http://ip.taobao.com/service/getIpInfo.php?ip=myip)

* POST: [http://ip.taobao.com/service/getIpInfo2.php?ip=myip](http://ip.taobao.com/service/getIpInfo2.php?ip=myip)

* GET: [http://pv.sohu.com/cityjson](http://pv.sohu.com/cityjson)
