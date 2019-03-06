# -*- coding: UTF-8 -*-
import requests
URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'
#多次请求重复使用一个socket，相比urllib。requests库会消耗更少的资源
def use_simple_requests():
    respose = requests.get(URL_IP)
    print respose.headers
    print respose.text

def user_params_requests():

    params = {'param1':'hello','param2':'world'}
    response = requests.get(URL_GET,params=params)
    print response.headers
    print response.status_code
    print response.reason
    print response.text

if __name__ == "__main__":
    use_simple_requests()
    user_params_requests()
