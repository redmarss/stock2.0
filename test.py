#!/bin/usr/env python
# -*-coding:utf-8 -*-

###############
#数据库操作类
#edit by redmars 20201115

import pymysql as pymysql
import pandas as pd

Class DBHelpler(object):
    #构造函数
    def __init__(self):
        #连接数据库
        try:
            self.conn = pymysql.connect{
                host = '127'
            }