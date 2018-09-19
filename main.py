#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from spyder import Feed
import db
import config


def get(target_mid):
    feed = Feed(target_mid, last_score=None)
    while True:
        feed_list = feed.get_next_feed_list()
        if not feed_list:
            break
        db.save_thread(feed_list, target_mid)


if __name__ == '__main__':
    get(config.mid_now)
    print('done')
