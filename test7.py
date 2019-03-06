# -*- coding: UTF-8 -*-
import re
#re.I匹配时忽略大小写
pa = re.compile(r'weinannan',re.I)
str  = "WEINANNAN jiayouha WEINANNAN youaresoclever"
ma = pa.match(str)
print ma.group()
print ma.span()


