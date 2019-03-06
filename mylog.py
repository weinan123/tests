# -*- coding: UTF-8 -*-
import logging
import os

# log_file = os.path.join(os.getcwd(),'wlog.log')
log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
'''
如果不写filename和filemode参数则默认打印到console
'''
logging.basicConfig(level=logging.WARNING, format=log_format)
# logging.basicConfig(level=logging.WARNING,format=log_format,filename=log_file,filemode='w')

logging.warning("waring message")
logging.error("error message")
