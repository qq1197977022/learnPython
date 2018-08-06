# 标准python解释器由C语言实现,python对象其实就是C语言中的结构体
# typedef struct_object {
#   int ob_refcnt;  //引用计数
#   struct_typeobject *ob_type;
# }

# python垃圾收集机制
#   1.itcast说法: 引用计数为主 + 标记-清除 和 分代收集为辅
#
#   2.官方文档
#       1.python拥有自动内存管理机制(引用计数+垃圾收集)
#           1.引用计数
#           2.循环垃圾收集器
#           3.弱引用
#       2.引用计数和循环垃圾收集器用于检测和消除循环引用
#       3.弱引用用于避免跟踪对象时额外产生的引用


class F(object):
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']

    def __getattr__(self, item):
        return 'getattr'

    def __getattribute__(self, item):
        raise AttributeError
        # return 'getattribute'


f1 = F(name='杨一帆', age=18)
print(f1.name)
print(f1.age)































