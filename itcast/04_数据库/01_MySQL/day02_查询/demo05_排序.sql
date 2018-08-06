# 查询未逻辑删除男生信息, 按学号降序排序
SELECT *
FROM student
WHERE gender=1 AND isDelete=0
ORDER BY id DESC ;


/*
1.默认升序
*/


































