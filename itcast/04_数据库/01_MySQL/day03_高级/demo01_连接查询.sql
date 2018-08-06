# 查询女生姓名, 总分
SELECT students.id, students.name, SUM(scores.grade) AS 总分
FROM students
  JOIN scores ON students.id = scores.stuid
WHERE students.gender=0
GROUP BY students.id;


SELECT *
FROM students
WHERE gender=1;

SELECT *
FROM students;
















