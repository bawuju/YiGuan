#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import configparser

# 配置
config = configparser.ConfigParser()
config.read('config.ini')

# 此刻
mid_now = 'N3ZOwLQXplgEdW82v0Bn'

# 恋爱
mid_love = 'R68LbZPMpA3yDYeNdOax'

# 丧
mid_bad = '4Jq3YdoNyG9pzw5MxPQ0'

# 秘密
mid_secret = 'QMwOWz6ayxJpGAbDxoLq'

# 自拍
mid_selfie = 'evwB0oDG7Rr739axJQ8n'

mid_name_map = {
    mid_now: '此刻',
    mid_love: '恋爱',
    mid_bad: '丧',
    mid_secret: '秘密',
    mid_selfie: '自拍'
}

mid_list = mid_name_map.keys()


def get_db_username():
    return config.get('db', 'db.username')


def get_db_password():
    return config.get('db', 'db.password')


def get_db_local():
    return config.get('db', 'db.local')


def get_db_port():
    return config.get('db', 'db.port')
