# conding=utf-8
'''
License: Copyright (c) Huawei Technologies Co., Ltd. 2012-2019.
All rights reserved.
Description: engine graph file parser
Date: 2019-5-26
LastEditTime: 2019-10-09 13:37:55
'''

import lib.config as config
import re
from lib.graph_exception import ParserError


def parse_mind_graph(mind_graph_file):
    p_eng = re.compile(r'engines')
    p_eng_name = re.compile(r'engine_name\s*:\s*"{1}(.*)"{1}')
    p_eng_id = re.compile(r'id\s*:\s*(.*)')
    p_eng_side = re.compile(r'side\s*:\s*(.*)')

    p_con = re.compile(r'connects')
    p_src_id = re.compile(r'src_engine_id\s*:\s*(.*)')
    p_target_id = re.compile(r'target_engine_id\s*:\s*(.*)')

    with open(mind_graph_file) as f:
        engines = {}  # 所有engine的属性信息
        engine_info = {}  # 每个engine的属性信息

        connects = []  # 所有engine的连接关系

        line = f.readline()
        while line:
            m_eng = re.search(p_eng, line)
            m_eng_id = re.search(p_eng_id, line)

            m_con = re.search(p_con, line)

            engine_info.clear()
            engine_map = []  # 两两连接关系

            #  engine part
            if m_eng and not m_eng_id:
                while line:
                    m_name = re.search(p_eng_name, line)
                    m_id = re.search(p_eng_id, line)
                    m_side = re.search(p_eng_side, line)
                    if m_name:
                        engine_info[config.ENGINE_NAME] = m_name.group(1)
                    if m_id:
                        id = m_id.group(1)
                        if id in engines.keys():
                            raise ParserError('''engine file is not correct, 
                                              please check it!''')
                        engine_info[config.ID] = m_id.group(1)
                    if m_side:
                        engine_info[config.SIDE] = m_side.group(1)
                    if len(engine_info) < 3:
                        line = f.readline()
                    else:
                        engine_info[config.ENGINE_SHOW_NAME] = \
                            engine_info[config.ENGINE_NAME] + config.SEP + \
                            engine_info[config.ID]
                        break
                engines[engine_info[config.ID]] = engine_info.copy()

            # connects part
            if m_con:
                while line:
                    m_src = re.search(p_src_id, line)
                    m_target = re.search(p_target_id, line)
                    if m_src:
                        engine_map.append((m_src.group(1)))
                    if m_target:
                        engine_map.append(m_target.group(1))
                    if len(engine_map) < 2:
                        line = f.readline()
                    else:
                        break
                connects.append(engine_map)

            line = f.readline()

        return engines, connects


if __name__ == '__main__':
    mind_graph_file_ = './graph.config'
    engines_, connects_ = parse_mind_graph(mind_graph_file_)
    print(engines_)
    print(connects_)
