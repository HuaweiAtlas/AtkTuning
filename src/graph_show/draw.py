# conding=utf-8
'''
License: Copyright (c) Huawei Technologies Co., Ltd. 2012-2019.
All rights reserved.
Description: 调用Graphviz生成可视化图形
Date: 2019-05-26
LastEditTime: 2019-10-09 13:37:16
'''

import argparse
import lib.config as config
import logging
import os
import sys
from graphviz import Digraph
from lib.graph_exception import ParserError
from lib.mind_graph_parser import parse_mind_graph


def draw_graph(mind_graph_file):
    if not os.path.exists(mind_graph_file):
        logging.error("graph engine file is not existed!")
        return False

    try:
        engines, connects = parse_mind_graph(mind_graph_file)
    except ParserError as parser_error:
        logging.error(parser_error.msg)
        return False
    except UnicodeDecodeError:
        logging.error("graph engine file parser failed!")
        return False
    except IOError:
        logging.error("graph engine file parser failed!")
        return False

    graph = Digraph(config.GRAPH_NAME, format=config.FORMAT)

    for k, v in engines.items():
        graph.attr('node', style='filled', shape=config.ENGINE_SHAPE)
        if v[config.SIDE] == config.SIDE_HOST:
            engine_color = config.HOST_COLOR
        elif v[config.SIDE] == config.SIDE_DEVICE:
            engine_color = config.DEVICE_COLOR
        else:
            logging.error("{}'s side is not correct! vs [side: {}]".format(
                v[config.ENGINE_NAME], v[config.SIDE]))
            return False
        graph.node(name=v[config.ENGINE_SHOW_NAME], color=engine_color)

    # graph lengend
    graph.node(name=config.SIDE_HOST, color=config.HOST_COLOR)
    graph.node(name=config.SIDE_DEVICE, color=config.DEVICE_COLOR)

    for con in connects:
        graph.attr('edge', color=config.LINE_COLOR)

        if len(con) != 2:
            logging.error("connects part is incorrect!")
            return False

        con1 = con[0]
        con2 = con[1]

        eng1 = engines.get(con1, "None")
        if eng1 == "None":
            logging.error("{} is not existed!".format(con1))
            return False

        eng2 = engines.get(con2, "None")
        if eng2 == "None":
            logging.error("{} is not existed!".format(con2))
            return False

        graph.edge(eng1[config.ENGINE_SHOW_NAME],
                   eng2[config.ENGINE_SHOW_NAME])

    graph.render(view=False)

    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        logging.error("the parameter number of command line must be one.")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('graph_config', help='graph config file path')
        args = parser.parse_args()

        status = draw_graph(args.graph_config)
        if not status:
            logging.error('''some error is encountered, 
            please check it by log file!''')
        else:
            logging.info(
                "{}(.svg) file have generated!".format(config.GRAPH_NAME))
