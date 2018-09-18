#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import configparser

# 配置
config = configparser.ConfigParser()
config.read('config.ini')


def get_db_username():
    return config.get('db', 'db.username')


def get_db_password():
    return config.get('db', 'db.password')


def get_db_local():
    return config.get('db', 'db.local')


def get_db_port():
    return config.get('db', 'db.port')
