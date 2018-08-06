DESCRIBE students;
DESCRIBE subjects;
DESCRIBE scores;
/*
一.连接操作
  1.支持语法
    1.DELETE: 删
    2.UPDATE: 改
    3.SELECT: 查
  2.ON 筛选连接数据集 ~ 笛卡尔积
  3.笛卡尔积
    1.INNER
    2.LEFT
    3.RIGHT
*/
# 查询每个学生各科分数
SELECT stuid, subid, grade
FROM scores;

SELECT students.id, students.name, subjects.name, scores.grade
FROM scores
JOIN students ON scores.stuid = students.id # 指定连接条件, 筛选连接数据集 ~ 笛卡尔积
JOIN subjects ON scores.subid = subjects.id
ORDER BY students.id ;
# ORDER BY scores.grade DESC ;

SELECT students.id, students.name, subjects.name, scores.grade
FROM students
JOIN scores ON students.id = scores.stuid
JOIN subjects ON scores.subid = subjects.id
ORDER BY students.id;

SELECT students.name, subjects.name, scores.grade
FROM scores
JOIN students, subjects  # 不指定连接条件
ORDER BY students.name;



INSERT INTO subjects (id, name) VALUES (0, 'GO+区块链');
INSERT INTO students (id, name, birthday) VALUES (8, 'C', '2008-8-3');
INSERT INTO scores (grade, stuid, subid) VALUES (12, 3, 7);

SELECT *
FROM scores;
ALTER TABLE subjects CHANGE name name VARCHAR(7) NOT NULL;
UPDATE scores SET grade=36 WHERE id=9;

DROP TABLE subjects, scores, students;


/*
一.外键级联操作
  1.删除students表数据, 若对应id在scores表已设置外键关联, 会抛出异常
  2.解决
    1.逻辑删除
    2.级联操作
      1.restrict: 限制 ~ 默认值, 抛出异常
      2.cascade: 级联 ~ 级联删除外键对应数据
      3.set null: 置空 ~ 将外键设置为空
      4.no action: 无视 ~ 什么都不做
*/
















