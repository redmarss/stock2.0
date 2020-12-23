#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:zwd
#DateTime:2020/11/17/16:30
#Project:Stock2.0/GlobalLib
#File:config.py

import os 

# 数据库连接
SQL_CONFIG = {
    "host" : "127.0.0.1",
    "port" : 3306,
    "db" : "tushare",
    "user" : "root",
    "passwd" : "redmarss111",
    "charset" : "utf8"
}

#获取根目录WORKSPACE_PATH 
curPath = os.path.dirname(os.path.abspath(__file__))        #globalConfig文件所在目录
WORKSPACE_PATH =  curPath[:curPath.find("stock2.0\\")+len("stock2.0\\")]     #获取根目录

