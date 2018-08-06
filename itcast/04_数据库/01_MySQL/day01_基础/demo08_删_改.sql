# 行更改
SELECT * FROM student;
UPDATE student SET name='秦晴', gender=0 WHERE name='杨一帆' ;
UPDATE student
SET name = '秦晴', gender=0
WHERE name='杨一帆';
UPDATE student SET name='杨一帆', gender=1 WHERE id<=3 ;


# 行删除
DELETE FROM student WHERE id>18;  # 物理删除
ALTER TABLE student ADD COLUMN isDelete BIT DEFAULT 0;
UPDATE student
SET student.isDelete = 1
WHERE id>=12; # 逻辑删除
/*
增加bit型, 标识逻辑删除的isDelete列, 约定
  1.0: 未删除
  2.1: 删除
*/
SELECT * FROM student WHERE isDelete=0; # 查询标识为未逻辑删除数据
SELECT * FROM student WHERE isDelete=1; # 查询标识为逻辑删除数据











