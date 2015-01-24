# -*-coding:utf-8-*-
__author__ = 'Long'

import os
import uuid
import urllib2
import json


# http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[[%22jjhq%22,1,40,%22%22,0,%22hs300%22]]&callback=
# http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[[%22hq%22,%22hs_a%22,%22%22,0,2,40]]&callback=

def get_file_extension(file):
    """获取文件后缀名"""
    return os.path.splitext(file)[1]


def mkdir(path):
    """創建文件目录，并返回该目录"""
    path = path.strip()
    path = path.rstrip("\\")
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def unique_str():
    """自动生成一个唯一的字符串，固定长度为36"""
    return str(uuid.uuid1())


def get_file(url):
    """
    抓取网页文件内容
    """
    try:
        opener = urllib2.build_opener()
        req = urllib2.Request(url)
        operate = opener.open(req)
        data = operate.read()
        return data
    except BaseException, e:
        print e
        return None


def save_file(path, file_name, data):
    """
    保存文件到本地
    @path  本地路径
    @file_name 文件名
    @data 文件内容
    """
    if data is None:
        return
    mkdir(path)
    if not path.endswith("/"):
        path += "/"
    file = open(path + file_name, "wb")
    file.write(data)
    file.flush()
    file.close()


if __name__ == '__main__':
    print('start download images ...')
    stocks_url = get_file(
        "http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[[%22jjhq%22,1,500,%22%22,0,%22hs300%22]]&callback=")
    json_stocks = json.loads(stocks_url)
    items = json_stocks[0]['items']
    for item in items:
        print(item[0] + " <->  " + item[1])
        url = "http://image.sinajs.cn/newchart/daily/n/" + item[0] + ".gif"
        save_file("stocks/", item[0] + "-" + item[1] + ".gif", get_file(url))