# 老司机经验总结
#   一.逻辑删除
#     1.物理删除的数据, 无法找回
#     2.因此对于重要数据, 并不希望物理删除; 而是增加一个bit类型的isDelete列, 表示逻辑删除
#       1.不展示标识为逻辑删除的数据 ~ 可通过在查询语句上增加条件实现
#   二.产品经理是条狗
#     1.一般在设计表时会在当前需求的基础上增加几行, 以应对可能的需求变化
#   三.区别对待
#     1.对于同一张表中数据, 按是否常用划分成两张表















