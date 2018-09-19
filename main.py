#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from spyder import Feed
import db
import config
import multiprocessing


def get(target_mid):
    feed = Feed(target_mid, last_score=None)
    while True:
        feed_list = feed.get_next_feed_list()
        if not feed_list:
            break
        db.save_thread(feed_list, target_mid)
    print('版块: %s 已完成' % config.mid_name_map[target_mid])


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=len(config.mid_list))
    for mid in config.mid_list:
        pool.apply_async(get, (mid,))
    pool.close()
    pool.join()
    print('所有进程执行完毕')
