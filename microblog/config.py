#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 17:19
# @Author  : wangyunchuan
# @File    : config.py
# @Project : microblog
# @Software: PyCharm


import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wangyunchuan'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')  # 数据库文件路径
    SQLALCHEMY_TRACK_MODIFICATIONS = False
