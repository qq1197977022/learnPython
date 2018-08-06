/*
一.事务
  1.事务是支持提交和回滚的原子工作单元 ~ 一组CUD操作
    1.原子工作单元: 即该组CUD操作都提交或都回滚即撤销
  2.事务用于管理CUD语句
    1.提交事务: 所有操作都成功
    2.回滚事务: 撤销所有操作
  3.由InnoDB实现的数据库事务具有四大特性: ACID
    1.原子性
    2.一致性
    3.隔离性
    4.持久性
  4.支持事务的数据库引擎
    1.InnoDB
  5.查看引擎信息
    1.查看可用存储引擎信息
      1.SHOW ENGINES
      2.SELECT * FROM INFORMATION_SCHEMA.ENGINES
    2.查看指定存储引擎操作信息
      1.SHOW ENGINE
二.事务语句
  1.begin: 开启事务
  2.commit: 结束并提交事务 ~ 永久保留事务所做的任何更改
  3.rollback: 结束并撤销事务 ~ 撤销对事务做的任何更改
三.事务过程? 原理? ~ 待解决
  1.
*/
# ------------------------当前连接A操作事务------------------------
SHOW CREATE TABLE test2;

ALTER TABLE test2 ENGINE = InnoDB;

START TRANSACTION ; # 开启一个新事务

UPDATE test2 SET gender = 1 WHERE name='杨一帆';

COMMIT ;  # 提交当前事务, 永久改变

SET AUTOCOMMIT = 0; # 0 开启/1 关闭自动提交

ROLLBACK ; # 回滚当前事务, 撤销所有改变
# ------------------------控制台新建B连接观察------------------------
SELECT sum(gender)
FROM test2
WHERE name='杨一帆';

SELECT SUM(gender)
FROM test2;
# ------------------------------------------------
/*
1.连接A操作事务, 连接B提交SQL, 连接C观察
2.发现会加锁 ~ 待总结
*/








































































