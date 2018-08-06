/*
聚合函数
  1.作用: 快速统计
  2.内置函数
    1.COUNT() 行数统计
    2.MAX() 最大值
    3.MIN() 最小值
    4.SUM() 求和
    5.AVG() 求平均值
*/

SELECT COUNT(*)
FROM student
WHERE id<12;

SELECT MAX(id)
FROM student;

SELECT MIN(id)
FROM student;

SELECT SUM(id)
FROM student;

SELECT AVG(id)
FROM student;

SELECT MAX(id)
FROM student
WHERE gender=1;

SELECT MIN(id)
FROM student
WHERE isDelete=1;


# 子查询
SELECT *
FROM student
WHERE id=(SELECT MIN(id)
          FROM student);


# 分组查询
SELECT COUNT(*)
FROM student
GROUP BY gender;

SELECT gender, COUNT(birthday) AS 生日
FROM student
GROUP BY gender;


SELECT gender, COUNT(name) AS 姓名
FROM student
WHERE id>1 GROUP BY gender;

SELECT isDelete, COUNT(name) AS 姓名, COUNT(birthday) AS 生日
FROM student
GROUP BY isDelete;

SELECT name AS 姓名, COUNT(gender) AS 性别
FROM student GROUP BY name;
SELECT name AS 姓名, COUNT(gender) AS 性别
FROM student GROUP BY name HAVING COUNT(gender)<3; # where筛选查询结果集, having筛选分组结果集
SELECT name AS 姓名, COUNT(gender) AS 性别
FROM student GROUP BY name HAVING 性别<3; # where筛选查询结果集, having筛选分组结果集


/*
1.分组查询
   1.select list项中的非group list项必须以聚合形式出现, 否则无法分组
     eg.假如select list中的name项为非group list项, 在分组时, 很多名字, 该显示哪个名字?
   2.当group list含有id项时, select list随意
2.where和having
    1.WHERE筛选原始数据集
    2.HAVING筛选查询结果集

3.SQL执行顺序
    FROM 原始数据集
    WHERE 筛选原始数据集 ~ WHERE筛选数据集
    GROUP BY 分组WHERE筛选数据集
    SELECT 查询结果集
    HAVING 筛选查询结果集
    ORDER BY 排序查询结果集
    LIMIT 分页查询结果集
*/






























