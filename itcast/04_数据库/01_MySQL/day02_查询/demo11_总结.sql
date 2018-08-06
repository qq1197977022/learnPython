# 查询学生姓名, 评价分数
SELECT students.id AS 学号, students.name AS 姓名, AVG(scores.grade) 平均分
FROM students
JOIN scores ON students.id = scores.stuid
GROUP BY students.id ;


SELECT *
FROM scores;



















































