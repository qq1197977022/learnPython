# 查看索引信息
SHOW INDEX IN students; # 默认当前数据库
SHOW INDEX IN scores IN python3;  # 指定数据库中表
SHOW INDEX IN python3.scores;  # 指定数据库中表

DESC students;

/*
开启性能分析: 参见SHOW PROFILE
  1.性能分析由session变量profiling控制
*/
SET PROFILING = 1;  # 0 关闭/1 开启

# 查看性能分析信息
SHOW PROFILE ALL ;
SHOW PROFILES ;

# 创建索引
CREATE INDEX areaName ON areas (name) ; # 单字段索引
ALTER TABLE areas RENAME INDEX areaName TO nameIndex; # 重命名索引
CREATE INDEX name_birth_Index ON students (name, birthday) ;  # 多字段索引

SELECT *
FROM areas
WHERE name='河南省';

SELECT *
FROM students
WHERE name='C' AND birthday='2008-08-03';
/*
一.简介
  1.一般应用系统, 读写比例在10:1左右, 且CUD操作很少出现性能问题, 所以R操作优化才是最关键的
  2.当数据量很大时, R操作性能降低, 通过索引可以提高R操作效率
  3.索引提高R效率, 但同时会降低CUD效率, 因为索引会建立索引文件, CUD操作除了要维护数据还要维护索引数据
二.技巧
  1.索引字段数据类型
    1.越小越好
    2.简单类型更好
    3.避免NULL
  2.SQL语句优化
    1.索引失效
      1.范围条件
      2.OR条件
    2.解决
        1.尽量不用
        2.置后 ~ 范围条件/OR条件置后
三.索引分类
  1.约束类型
    1.主键索引
    2.唯一索引
  2.实现分类
    1.单字段索引
      1.索引:字段 = 1:1
      2.一个表可包含多个单列索引
    2.多字段索引 组合索引
      1.索引:字段 = 1:n

*/

































































