#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import time
import sys


def stop():
    """
    退出进程
    :return: None
    """
    sys.exit(0)


def print_json(content):
    """
    将decode的对象输出到控制台
    :param content: decode的对象或者str
    :return: None
    """
    content_str = str(content) if not isinstance(content, str) else content
    print(content_str.replace("'", '"').replace('False', '"False"').replace('True', '"True"'))


def print_time(content):
    """
    将一罐内容里的时间格式化之后输出到控制台
    :param content: decode的对象
    :return: None
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(content['createTime']))
