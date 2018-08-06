/*
范围查询
  1.IN 成员测试
  2.BETWEEN...AND... 区间
*/
SELECT *
FROM student
WHERE id IN (1, 4, 5, 7, 9, 11);  # 成员测试

SELECT *
FROM student
WHERE id NOT IN (1, 4, 5, 7, 9, 11);

SELECT * FROM student
WHERE id BETWEEN 1 AND 11;  # 区间

SELECT *
FROM student
WHERE id NOT BETWEEN 1 AND 11;

SELECT * FROM student
WHERE id BETWEEN 1 AND 18
      AND isDelete = 1;

/*
判空
  1.NULL不同于空串"" ~ NULL不占内存, 空串占用内存
*/
SELECT *
FROM student
WHERE birthday IS NULL ;

SELECT *
FROM student
WHERE birthday IS NOT NULL ;












