# 1.查看当前数据库 db
# 2.查看可用数据库
#   1.mongo Shell: show dbs| databases
#   2.命令: listDatabases
# 3.切换数据库use <database>
#     1.可以切换到不存在数据库, 但在创建集合或插入文档时才会创建
#     2.默认使用的test数据库实际也是不存在的
# 4.执行命令
#   1.针对当前数据库执行: db.runCommand()
#   2.针对admin数据库执行: db.adminCommand()
# 4.删除当前数据库
#   1.命令: dropDatabase
#   2.包装方法: db.dropDatabase()
# 5.创建集合/ 视图
#   1.命令: create
#   2.包装方法: db.createCollection()| db.createView()
# 6.查看集合
#   1.mongo Shell: show collections
#   2.命令: listCollections
#   3.包装方法
#     1.gb.getCollectionInfos()
#     2.db.getCollectionNames()
# 7.删除集合
#   1.命令: drop
#   2.包装方法: db.collection.drop()


# 数据类型
#   1.ObjectId
#   2.


# 15:...








































