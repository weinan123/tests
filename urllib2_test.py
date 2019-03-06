# -*- coding: UTF-8 -*-
import urllib
import urllib2
URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'
def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print response.info()
    print ''.join([line for line in response.readlines()])
def use_params_urllib2():
    # 构建请求参数
    params = urllib.urlencode({'param1':'hello','param2':'world'})
    print params
    # 发送请求
    response = urllib2.urlopen('?'.join([URL_GET,'%s'])% params)
    # 处理响应
    print response.info()
    print response.getcode()
    #请求变为字符串
    print ''.join([line for line in response.readlines()])

if __name__ == "__main__":
    use_simple_urllib2()
    use_params_urllib2()





