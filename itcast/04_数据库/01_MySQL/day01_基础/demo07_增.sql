SELECT database();
# 查询
SELECT * FROM student;
SELECT id FROM test2;
SELECT all * FROM test2;
SELECT all id FROM test2;


# 增加数据
DESCRIBE student;
INSERT student VALUE (0, '杨一帆', 1, '2018-5-6'); # 全字段插入
INSERT student VALUES (0, '杨一帆', 1, '2018-5-6');
INSERT student VALUES (0, '秦晴', 0, '2018-5-6');
INSERT student VALUES (8, '秦晴', 0, '2018-5-6');
INSERT INTO student VALUES (8, '秦晴', 0, '2018-5-6');
INSERT INTO student VALUES (0, '脑残', 0, '2018-5-6');

INSERT student (name, gender) VALUES ('范冰冰', 0);  # 部分字段插入
INSERT INTO student (name, gender) VALUES ('范冰冰', 0);

INSERT INTO student VALUES (0, '范冰冰', 0, '2008-1-2'), (0, '李晨', 1, '2018-2-1'), (0, '高晓松', 1,'1990-3-5'); # 多行全字段插入
INSERT INTO student (name) VALUES ('SHE'), ('李纹'), ('林楠'), ('曾伟楠'); # 多行部分字段插入

DELETE FROM student WHERE id = 9; # 删除行
/*
1.约定bit型的gender列
  1.1: 男
  2.0: 女
2.auto_increment约束
  1.0: 自动增长
  2.number: 自定义
*/



























