/*
一.视图
  1.问题: 复杂查询, 维护非常麻烦
  2.解决: 视图
  3.本质: 对查询结果集的封装 ~ 提高复用性
  4.语法
*/

SHOW TABLES ;
SELECT *
FROM scores
JOIN students s ON scores.stuid = s.id
JOIN subjects s2 ON scores.subid = s2.id;


# 创建视图
CREATE VIEW v1
  AS
    SELECT students.id, students.name AS stuName, subjects.name AS subName, scores.grade
    FROM students
      JOIN scores ON students.id = scores.stuid
      JOIN subjects ON scores.subid = subjects.id
    ORDER BY students.id;

SHOW TABLES ;

SELECT *
FROM v1;

DROP VIEW v1;

# 基于视图查询
SELECT *
FROM v1
WHERE stuName='A';







































