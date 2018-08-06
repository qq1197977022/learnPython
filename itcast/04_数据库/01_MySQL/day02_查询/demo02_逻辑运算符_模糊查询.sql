SELECT *
FROM student;

# 查询id>3
SELECT *
FROM student
WHERE id > 3;
# 查询id<3或没有被逻辑删除
SELECT *
FROM student
WHERE id<3 OR isDelete=0;

SELECT *
FROM student
WHERE id<3 || isDelete=0;


SELECT *
FROM student
WHERE id<5
      AND name LIKE '%一%';

SELECT *
FROM student
WHERE id>5
      AND name NOT LIKE '%晴%'
      AND name NOT LIKE '%冰%';
/*
模糊查询
  1.LIKE 简单模式匹配
  2.NOT LIKE 反向模式匹配
  3.通配符
    1.% 匹配0<=个字符
    2._ 匹配单个字符
*/



