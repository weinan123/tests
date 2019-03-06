# -*- coding: UTF-8 -*-
import logging
#创建一个logger
logger = logging.getLogger('mylog2')
logger.setLevel(logging.INFO)
#创建一个handle.将log写入文件
fh = logging.FileHandler('C:/Users/nan.wei/Desktop/123.txt','a')
fh.setLevel(logging.INFO)
#再创建一个handle,将log输出在控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
#设置输出格式
log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
#把handle添加到logger里，其实可以理解为回报给大领导
logger.addHandler(fh)
logger.addHandler(ch)
logger.error("今天天气不好哦")