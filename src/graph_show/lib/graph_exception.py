# conding=utf-8
'''
License: Copyright (c) Huawei Technologies Co., Ltd. 2012-2019.
All rights reserved.
Description: exception definition
Date: 2019-09-18 23:36:54
LastEditTime: 2019-10-09 11:25:46
'''


class ParserError(Exception):
    '''
    解析graph文件异常
    '''

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
