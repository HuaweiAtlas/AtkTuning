# conding=utf-8
'''
License: Copyright (c) Huawei Technologies Co., Ltd. 2012-2019.
All rights reserved.
Description: 属性等配置信息
Date: 2019-05-26
LastEditTime: 2019-10-09 12:05:39
'''

import logging

logger = logging.getLogger()
logger.setLevel('DEBUG')
BASIC_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
chlr = logging.StreamHandler()  # 输出到控制台的handler
chlr.setFormatter(formatter)
chlr.setLevel('DEBUG')  # 也可以不设置，不设置就默认用logger的level
fhlr = logging.FileHandler('graph_show.log')  # 输出到文件的handler
fhlr.setFormatter(formatter)
logger.addHandler(chlr)
logger.addHandler(fhlr)

GRAPH_NAME = 'EngineFlow'
FORMAT = 'svg'  # svg, png

#  engine attr config
ID = 'id'
ENGINE_NAME = 'engine_name'
SIDE = 'side'
SIDE_HOST = 'HOST'
SIDE_DEVICE = 'DEVICE'

SEP = '-'
ENGINE_SHOW_NAME = "engine_show_name"

#  color config
ENGINE_SHAPE = 'box'
RED = 'red'
GREEN = 'green'
BLUE = 'blue'

DEVICE_COLOR = 'green3'
HOST_COLOR = 'dodgerblue'

LINE_COLOR = 'black'
