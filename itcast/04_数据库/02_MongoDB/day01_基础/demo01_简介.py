# MongoDB
#   一.简介
#     1.基于分布式的文档存储NoSQL数据库
#     2.C++编写, 稳定高效
#     3.高可扩展, 高性能
#     4.将数据存储为类似JSON对象的文档, 数据有键值对组成, 值可包含其他文档, 数组, 文档数组
#   二.特点
#     1.模式自由: 同一数据库可存储不同结构文件
#     2.面向集合存储: JSON风格文件
#     3.完整索引支持: 对任何属性均可索引
#     4.复制和高可用
#       1.服务器间数据复制
#       2.主从模式及服务器间互相复制
#       3.复制目的: 提供冗余及故障转移
#     5.自动分片
#       1.支持云支持级别伸缩性
#       2.支持水平数据库集群, 可动态添加额外机器
#     6.语法丰富: 查询指令使用JSON形式的标记, 可轻易查询文档中内嵌对象及数组
#     7.高效的传统存储方式: 支持二进制数据及大型对象(照片, 视频等)
#   三.术语对比
#     MySQL                     MongoDB
#       database                    database        数据库
#       table                       collection      表/集合
#       row                         document        记录行/文档
#       column                      field           列字段/域
#       index                       index           索引
#       table join                  不支持           表连接
#                                     1.因为NoSQL非E-R模型, 不维护实体/表间关系
#       primary key                 primary key     主键 MongoDB自动将_id域设置为主键
#   四.三元素
#     1.数据库: database
#       1.集合容器
#     2.集合: collection
#       1.文档集合
#       2.结构不固定
#     3.文档: row
#       1.键值对对象, 是JSON的Bson扩展形式
#

# NoSQL
#   1.Not Only SQL: 非关系型数据库
# 一.优点
#   1.高可扩展
#   2.分布式
#   3.低成本
#   4.构建灵活, 半结构化数据
#   5.没有复杂的关系
# 二.缺点
#   1.没有标准化
#   2.查询功能有限
#   3.最终一致是不直观的程序


# 一般部署方式
#   1.用户 ---> WebApp ---> 内存级缓存数据库redis/MongoDB ---> 硬盘持久化数据库MySQL


# 常见数据库分类
#   一.列存储
#     1.Hbase
#     2.Cassandra
#     3.Hypertable
#     特点:
#       1.按列存储
#       2.方便存储结构化/半结构化数据, 方便数据压缩
#       3.针对列查询IO优势明显
#   二.文档存储
#     1.MongoDB
#     2.CouchDB
#     特点:
#       1.类JSON格式存储
#       2.便于对字段建立索引, 实现关系型数据库某些功能
#   三.key-value存储
#     1.Tokyo Cabinet / Tyrant
#     2.Berkeley DB
#     3.MemacheDB
#     4.Redis
#     特点:
#       1.通过key快速查找value
#   四.图存储
#     1.Neo4J
#   五.XML数据库
#     1.Berkeley DB XML
#     2.BaseX
#     特点:
#       1.高效XML数据存储
#       2.支持XML语法


























































