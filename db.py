#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from sqlalchemy import Column, String, create_engine, BIGINT, INT, SMALLINT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
import config
import tools

# 创建对象的基类:
Base = declarative_base()


# 定义Thread对象:
class Thread(Base):
    # 表的名字:
    __tablename__ = 'thread'

    # 表的结构:
    primary_id = Column(BIGINT(), primary_key=True, autoincrement=True)
    id = Column(String(20), default='')
    mid = Column(String(20), default='')
    tid = Column(String(20), default='')
    text = Column(String(2048), default='')
    age = Column(String(8), default='')
    gender = Column(INT(), default=0)
    photos = Column(String(2048), default='')
    nickname = Column(String(32), default='')
    weather = Column(String(16), default='')
    temperature = Column(String(16), default='')
    createTime = Column(BIGINT(), default=0)
    likedNum = Column(INT(), default=0)
    commentedNum = Column(INT(), default=0)
    isLiked = Column(SMALLINT(), default=0)
    score = Column(String(20), default='')
    isTop = Column(SMALLINT(), default=0)


# 初始化数据库连接:
engine = create_engine(
    'mysql+pymysql://%s:%s@%s:%s/yi_guan' %
    (config.get_db_username(), config.get_db_password(), config.get_db_local(), config.get_db_port()),
    pool_size=20, max_overflow=0)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def save_thread(feed_list, mid):
    """
    保存一罐的内容
    :param feed_list: decode的对象
    :param mid: 版块id
    :return: None
    """
    success = 0
    failed = 0
    for content in feed_list:
        session = DBSession()
        try:
            new_thread = Thread(id=content['id'], tid=content['tid'], mid=mid, text=content['text'], age=content['age'],
                                gender=content['gender'], photos=str(content['photos']), nickname=content['nickname'],
                                weather=content['weather'], temperature=content['temperature'],
                                createTime=content['createTime'],
                                likedNum=content['likedNum'], commentedNum=content['commentedNum'],
                                isLiked=content['isLiked'],
                                score=content['score'], isTop=content['isTop'])
            session.add(new_thread)
            session.commit()
            success += 1
        except IntegrityError as e:
            failed += 1
            if 'Duplicate entry' in str(e):
                pass
            else:
                print('============================================================')
                print(str(e))
                print('============================================================')
                raise e
        session.close()
    current_time = tools.print_time(feed_list[-1])
    print('时间: %s, 版块: %s, 成功: %s, 失败: %s' % (current_time, config.mid_name_map[mid], success, failed))


def get_thread_score(mid, last=True):
    """
    获取最后一条score
    :param mid: 版块id
    :param last: 是否最后一条
    :return: score
    """
    order = Thread.createTime if last else desc(Thread.createTime)
    session = DBSession()
    thread = session.query(Thread).filter(Thread.mid == mid).order_by(order).first()
    session.close()
    return None if thread is None else thread.score
