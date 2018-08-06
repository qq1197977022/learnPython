/*
一.备份
  1.mysqldump -u root -p (database [table_list]) > path\back.sql
  2.备份方式
    1.整库备份
    2.表备份
      1.单表
      2.多表
*/


/*
二.恢复
  1.方式一: mysql -u root -p database < path\back.sql
  2.方式二: 登录 ---> source path\back.sql
  3.恢复方式
    1.表恢复
    2.库恢复
*/
CREATE DATABASE python31;
SHOW DATABASES ;
USE python31;
SHOW TABLES ;
SELECT * FROM student;






















