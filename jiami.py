# -*- coding: UTF-8 -*-
import hashlib
import base64
def md5_encode(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()
data = 'wo'
print (u'md5加密结果：',md5_encode(data))