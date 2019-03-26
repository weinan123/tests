#-*- coding:utf-8 –*-
import requests
import json
#key-value
url = "http://v.juhe.cn/laohuangli/d"
para = {"key":"eeeeeeeeeeeeeeee","date":"2017-3-22"}
header = {}
r = requests.get(url,params=para,headers=header)
print (u'get请求获取的响应结果json类型',r.text)
print (u"get请求获取响应状态码",r.status_code)
print (u'get请求获取响应头',r.headers['Content-Type'])
json_r = r.json()
print (json_r)
#json
url = "http://v.juhe.cn/laohuangli/d"
para = {"key":"eeeeeeeeeeeeeeee","date":"2017-3-22"}
header = {}
para = json.dumps(para)
r = requests.post(url,params=para,headers=header)
print (u'get请求获取的响应结果json类型',r.text)
print (u"get请求获取响应状态码",r.status_code)
print (u'get请求获取响应头',r.headers['Content-Type'])
json_r = r.json()
print (json_r)