#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from spyder import Feed
import db

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

mid_list = [mid_now, mid_love, mid_bad, mid_secret, mid_selfie]


def get(target_mid):
    feed = Feed(target_mid, last_score=None)
    while True:
        feed_list = feed.get_next_feed_list()
        if not feed_list:
            break
        db.save_thread(feed_list, target_mid)


if __name__ == '__main__':
    get(mid_now)
    print('done')
