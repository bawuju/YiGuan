# 爬取一罐的罐子详情

## USAGE

1. 创建数据库配置文件`config.ini`
    
    > 参见config.ini.template
   
2. 运行`main.py`

## 库&表结构

```sql
CREATE DATABASE `yi_guan`;
CREATE TABLE `thread` (
  `primary_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `id` varchar(20) DEFAULT NULL COMMENT '帖子id',
  `mid` varchar(20) DEFAULT NULL COMMENT '版块id',
  `tid` varchar(20) DEFAULT NULL COMMENT '不知道什么东西',
  `text` varchar(2048) DEFAULT NULL COMMENT '正文',
  `age` varchar(8) DEFAULT NULL COMMENT '年龄',
  `gender` int(11) DEFAULT NULL COMMENT '性别',
  `photos` varchar(2048) DEFAULT NULL COMMENT '附带的照片',
  `nickname` varchar(32) DEFAULT NULL COMMENT '昵称',
  `weather` varchar(16) DEFAULT NULL COMMENT '当地天气',
  `temperature` varchar(16) DEFAULT NULL COMMENT '当地气温',
  `createTime` bigint(20) DEFAULT NULL COMMENT '创建时间',
  `likedNum` int(11) DEFAULT NULL COMMENT '点赞数',
  `commentedNum` int(11) DEFAULT NULL COMMENT '评论数',
  `isLiked` smallint(6) DEFAULT NULL COMMENT '是否被点赞。只有登录才有效，所以爬取的时候这个字段无效',
  `score` varchar(20) DEFAULT NULL COMMENT '分页依据',
  `isTop` smallint(6) DEFAULT NULL COMMENT '是否被置顶',
  PRIMARY KEY (`primary_id`),
  UNIQUE KEY `id` (`id`,`createTime`,`mid`),
  KEY `idx_id` (`id`),
  KEY `idx_mid` (`mid`),
  KEY `idx_age` (`age`),
  KEY `idx_nickname` (`nickname`),
  KEY `idx_createTime` (`createTime`),
  KEY `idx_likedNum` (`likedNum`),
  KEY `idx_score` (`score`)
) ENGINE=InnoDB AUTO_INCREMENT=485532 DEFAULT CHARSET=utf8mb4 COMMENT='一罐帖子表';
```
