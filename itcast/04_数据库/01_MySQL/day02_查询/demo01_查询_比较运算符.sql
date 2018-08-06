SELECT database();
SHOW TABLES ;
SELECT id FROM student;
SELECT id, name FROM student;
SELECT id AS 编号, name AS 姓名 FROM student;

SELECT gender
FROM student;

SELECT
  DISTINCT gender
FROM student; # 去重查询

SELECT
  DISTINCTROW *
FROM test2;

SELECT *
FROM student
WHERE id<=8; # 条件查询

SELECT *
FROM student
WHERE name='杨一帆';
/*
一.相关概念
  1.原始数据集
  2.查询结果集 ~ 查询得到的结果表, 物理不存在
*/


# 参见: https://dev.mysql.com/doc/refman/8.0/en/functions.html











