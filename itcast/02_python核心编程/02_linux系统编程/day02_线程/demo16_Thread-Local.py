# 线程业务复杂调用多个函数
#   1.传参: 麻烦
#   2.不传参
#       1.全局变量: 存在竞争状态, 不能保证对共享资源的安全访问
#       2.全局字典: key = 当前线程唯一标识, 可行
#       3.Thread-Local Data

import threading


def fun1(name, age, gender):
    print(f'{name}\t{age}\t{gender}')


def fun1_1():
    fun1('杨一帆', 18, '男')


def fun1_2():
    fun1('秦晴', 16, '女')


def main(tar1, tar2):
    t1 = threading.Thread(target=tar1)
    t2 = threading.Thread(target=tar2)
    t1.start()
    t2.start()
# -----------------------------------------------------------------------------------------------


def fun2():
    man = g_dic[threading.current_thread().name]
    print(f'{man["name"]}\t{man["age"]}\t{man["gender"]}')


def fun2_1():
    g_dic[threading.current_thread().name] = {'name': '范冰冰', 'age': 38, 'gender': '女'}
    fun2()


def fun2_2():
    g_dic[threading.current_thread().name] = {'name': '李晨', 'age': 39, 'gender': '男'}
    fun2()
# -----------------------------------------------------------------------------------------------


def fun3():
    print(f'{tld.name}\t{tld.age}\t{tld.gender}')


def fun3_1():
    tld.name = '苍老师'
    tld.age = 56
    tld.gender = '女'
    fun3()


def fun3_2():
    tld.name = '安倍晋三'
    tld.age = 66
    tld.gender = '狗'
    fun3()


if __name__ == '__main__':
    # 方式一: 传参
    # main(fun1_1, fun1_2)

    # 方式二: 全局字典
    g_dic = {}
    # main(fun2_1, fun2_2)

    # 方式三: Thread-Local Data, 面向对象
    tld = threading.local()
    main(fun3_1, fun3_2)

















