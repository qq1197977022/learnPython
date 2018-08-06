CREATE TABLE stu (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  name VARCHAR(5) NOT NULL ,
  gender BIT NOT NULL DEFAULT 0,
  birthday DATE,
  isDel BIT NOT NULL DEFAULT 0
);

CREATE TABLE subjects (
  id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  name VARCHAR(5) NOT NULL
);

CREATE TABLE scores (
  id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  grade FLOAT(5, 2) NOT NULL,
  stuid INT(3) NOT NULL , # 关系字段
  subid INT(3) NOT NULL ,
  FOREIGN KEY (stuid) REFERENCES students (id), # 关系存储
  FOREIGN KEY (subid) REFERENCES subjects (id)
);


SELECT database();
SHOW TABLES ;
DESC scores;
ALTER TABLE students CHANGE COLUMN name name VARCHAR(5) NOT NULL ;
DROP TABLE scores;
























































