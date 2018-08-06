# 参见: https://dev.mysql.com/doc/refman/8.0/en/func-op-summary-ref.html
# MySQL服务器版本
SELECT version();
# 当前日期时间
SELECT now();
# 当前使用的数据库
SELECT DATABASE();
# 退出: exit / quit

USE python3;


# 创建数据库
CREATE DATABASE test CHARSET = utf8;
CREATE DATABASE test1 CHARACTER SET utf8;


# 创建表
CREATE TABLE student
(
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL ,
  name VARCHAR(5) NOT NULL ,
  gender BIT DEFAULT 0,
  birthday DATE
) CHARACTER SET UTF8;
SHOW TABLES ;
DROP TABLE student;


# 表结构
DESCRIBE student;
SHOW COLUMNS in student;
SHOW COLUMNS FROM student;
EXPLAIN student;


# SQL语句
SHOW CREATE DATABASE python3;
SHOW CREATE TABLE student;


# 修改表结构
ALTER TABLE student ADD COLUMN isDelete BIT DEFAULT 0;
ALTER TABLE student DROP COLUMN isDelete;
ALTER TABLE student RENAME TO test1;  # 重命名表名
RENAME TABLE test1 TO test2;  # 重命名表名
ALTER TABLE student CHANGE COLUMN isDelete deleteFlag BIT DEFAULT 0;  # 修改列
ALTER TABLE student RENAME COLUMN deleteFlag TO isDelete; # 仅重命名列

































