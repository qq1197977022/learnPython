# 图书表结构
#   表名: Book
#   图书名: name
#   图书发布日期: date
# 英雄表结构
#   表名: Hero
#   英雄姓名: name
#   英雄性别: gender
#   英雄简介: introduce
#   所属图书: book
# E-R模型
#   E:
#     1.图书
#     2.英雄
#       R n:1 ~ 多对一
# Models映射关系
#   1.类对象: 表
#   2.类对象数据属性: 表字段
#       1.因此仅CURD类对象数据属性时才需要migrate, CURD方法无需migrate ~ 不对应数据库数据
#       2.id字段会默认自动添加
#   3.实例对象: 数据记录
#





























































