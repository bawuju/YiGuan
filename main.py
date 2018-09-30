#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from spyder import Feed
import db
import config
import multiprocessing
import tools
import time


def get(target_mid):
    feed = Feed(target_mid, last_score=None)
    while True:
        feed_list, request_time, decode_time = feed.get_next_feed_list()
        if not feed_list:
            break
        save_time_start = time.time()
        success, failed = db.save_thread(feed_list, target_mid)
        save_time = time.time() - save_time_start
        last_time = tools.print_time(feed_list[-1])
        print('最后一条的时间: %s, 版块: %s, 成功: %s, 失败: %s, 请求耗时 %.3f 秒, 解析耗时 %.3f 秒, 保存耗时 %.3f 秒' %
              (last_time, config.mid_name_map[target_mid], success, failed, request_time, decode_time, save_time / len(feed_list)))
    print('版块: %s 已完成' % config.mid_name_map[target_mid])


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=len(config.mid_list))
    for mid in config.mid_list:
        pool.apply_async(get, (mid,))
    pool.close()
    pool.join()
    print('所有进程执行完毕')
