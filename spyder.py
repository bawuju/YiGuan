#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import demjson
import requests
import config

headers = {
    'User-Agent': 'guan/1.3.1 (club.jijigugu.yiguan; build:212; iOS 11.4.1) Alamofire/4.7.0'
}


class Feed:

    def __init__(self, mid, last_score=None):
        """
        获取一罐内容
        :param mid: 版块的mid
        :param last_score: 上一条内容的score
        """
        self.url = 'https://api.jijigugu.club/feed/list?platform=2&mid=' + mid
        self.last_score = last_score
        self.is_end = False
        self.name = config.mid_name_map[mid]

    def get_feed_url(self, last_score):
        """
        获取请求地址
        :param last_score: 上一条内容的score
        :return: url
        """
        return self.url + '&lastScore=' + last_score if last_score else self.url

    def get_next_feed_list(self):
        """
        获取下一页内容
        获取成功后会自动设置last_score
        :return: 经过decode之后的对象
        """
        if self.is_end:
            return []
        url = self.get_feed_url(self.last_score)
        while True:
            try:
                r = requests.get(url, headers=headers, verify=True)
                break
            except Exception as e:
                print('产生异常 = %s, 版块 = %s, 重试中...' % (str(e), self.name))
        data = demjson.decode(r.text)['data']
        if not data:
            self.is_end = True
            return []
        self.last_score = data[-1]['id']
        return data


class Comment:
    def __init__(self):
        self.url = 'https://api.jijigugu.club/comment/list?platform=2'

    def get_comment_url(self, did, last_score=None):
        url = self.url + '&did=' + did
        return url if not last_score else url + '&lastScore=' + last_score

    def get_all_comment(self, did):
        r = requests.get(self.get_comment_url(did), headers=headers, verify=True)
        result = demjson.decode(r.text)['data']
        if not result:
            return result
        while True:
            r = requests.get(self.get_comment_url(did, result[-1]['id']), headers=headers, verify=True)
            sub_result = demjson.decode(r.text)['data']
            if not sub_result:
                break
            result.extend(sub_result)
        return result
