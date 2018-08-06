SHOW DATABASES ;
SELECT DATABASE();
SHOW TABLES ;


/*
一.分页查询
  1.offset从0开始计数
    1.limit n*m, m: 从第0页开始, 每页显示m条数据
    2.limit (n-1)*m, m: 从第1页开始, 每页显示m条数据
*/
SELECT *
FROM student LIMIT 5; # row_count 等价 0, 5 或 5 OFFSET 0

SELECT *
FROM student LIMIT 2, 5;  # offset, row_count

SELECT *
FROM student LIMIT 5 OFFSET 2;  # row_count OFFSET offset ~ MySQL为支持PostgreSQL而添加语法支持


SELECT id
FROM student;

INSERT INTO student SET name="B", id=9;

DELETE FROM student WHERE id=18;

SELECT *
FROM student;

