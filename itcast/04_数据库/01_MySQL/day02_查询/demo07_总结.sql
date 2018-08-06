/*
参见: https://www.cnblogs.com/annsshadow/p/5037667.html

一.执行顺序
  FROM <left_table>
  ON <join_condition>
  <join_type> JOIN <right_table>
  WHERE <where_condition>
  GROUP BY <group_by_list>
  HAVING <having_condition>
  SELECT
  DISTINCT <select_list>
  ORDER BY <order_by_condition>
  LIMIT <limit_number>


SQL执行顺序
  1.FROM 原始数据集
  2.ON 筛选原始数据集, 得到ON筛结果选集
  3.JOIN 连接ON筛选结果集, 得到连接结果集
  4.WHERE 筛选连接结果集, 得到WHERE筛结果选集
  5.GROUP BY 分组WHERE筛选结果集, 得到分组结果集
  6.SELECT 查询分组结果集, 得到查询结果集
  7.HAVING 筛选分组结果集, 得到HAVING筛选结果集
  8.ORDER BY 排序HAVING筛选结果集, 得到ORDER排序结果集
  9.LIMIT 分页ORDER排序结果集
*/


































