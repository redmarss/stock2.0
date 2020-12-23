#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import os
from GlobalLib.globalConfig import WORKSPACE_PATH
from GlobalLib.myTime import strToday


class mylogger(object):
    date = strToday()
    #clevel代表控制台报错级别，flevel代表文件报错级别
    def __init__(self, filepath=f'log\{date}.log', clevel=logging.DEBUG, flevel=logging.ERROR):
        fullpath = WORKSPACE_PATH+filepath
        print(fullpath)
        #文件夹不存在，则创建文件夹
        path = WORKSPACE_PATH+'log'
        if not os.path.exists(path):
            os.mkdir(path)
        # 文件不存在，则创建文件
        if not os.path.exists(fullpath):
            f = open(fullpath, 'a+')
            f.close()

        print()
        self.logger = logging.getLogger(filepath)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s]-[%(name)s]-[%(levelname)s]:[%(message)s]','%Y-%m-%d %H:%M:%S')
        #设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        #设置文件日志
        fh = logging.FileHandler(fullpath)
        fh.setFormatter(fmt)
        fh.setLevel(flevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warnning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)