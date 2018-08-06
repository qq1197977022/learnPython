# 查询各科平均分
SELECT subjects.name AS 科目, AVG(scores.grade) AS 平均分
FROM subjects
JOIN scores ON scores.subid = subjects.id
GROUP BY subjects.name;

SELECT subjects.id AS 科目编号, subjects.name AS 科目, AVG(scores.grade) AS 平均分
FROM subjects
JOIN scores ON scores.subid = subjects.id
GROUP BY subjects.id;


# 查询未删除科目名称, 最高分, 平均分, 总分
DESC subjects;
ALTER TABLE subjects ADD COLUMN isDel BIT NOT NULL DEFAULT 0;
SELECT *
FROM subjects;
UPDATE subjects SET subjects.isDel=1 WHERE id%2=0 AND id<5;

SELECT subjects.name AS 科目, MAX(scores.grade) AS 最高分, AVG(scores.grade) AS 平均分, SUM(scores.grade) AS 总分, subjects.isDel
FROM subjects
JOIN scores ON subjects.id = scores.subid
WHERE subjects.isDel=0
GROUP BY subjects.id;

SELECT scores.id, scores.stuid
FROM scores;


# ---------------------自关联---------------------
/*
国家  country
省    province
市    city
区/县 county
镇    town
村    village

province表结构
  id
  name
city表结构
  id
  name
  pro_id

问题: 能否将两个表合成一张表?
思考: 观察发现, city表笔province表多了一个pro_id字段, 其他字段完全一致(名, 类型)
意义: 都是存储地区信息, 且每种信息数量都有限, 没必要创建新表增加开销(假如存还要存储区/县, 乡镇, 村信息都建新表, 开销大大增加)
答案: 合成一张areas表 ~ 自关联, 表中某列关联了该表中另一列(city id引用province id), 但其业务逻辑不一样
        id
        name
        pid ~ parent id
  1.市pid字段为对应省份id
  2.pid字段对于省无意义, 设置为NULL
  3.表结构不变, 还可以添加区县, 乡镇, 村, 社区等信息
*/

# 物理一张表, 逻辑N张表 ~ 省表, 市表, 区县表....
CREATE TABLE areas (
  id INT(2) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(8) NOT NULL ,
  pid INT(2) DEFAULT NULL ,
  FOREIGN KEY (pid) REFERENCES areas (id)
);


# 一.查询河南省所有市
/*
普通查询
  1.where过滤后的原始数据集, name字段不包含省, 全是pid=1的所有市名称
  2.因而普通查询不能同时查询到市名称和省名称
*/
SELECT areas.pid AS 省编号, areas.id AS 市编号, areas.name AS 市  # 普通查询
FROM areas
WHERE areas.pid=1;

/*
自连接查询
  1.把一张物理表, 看做N张逻辑表
  2.这里是看做两张表
    1.Province表
    2.City表
    3.Note
      1.通过别名把一张物理表分成两张逻辑表(Province, City)
      2.同名字段在不同逻辑表中具有不同含义
        eg. name字段
          1.在Province表中表示省名称
          2.在City表中表示City名称
*/
SELECT Province.id AS 省编号, Province.name AS 省, City.id AS 市编号, City.name AS 市
FROM areas AS Province
  JOIN areas City ON Province.id = City.pid
WHERE City.pid=3;


# 子查询: select查询嵌套
SELECT *
FROM student
WHERE id=(SELECT MAX(id)
          FROM student);





















