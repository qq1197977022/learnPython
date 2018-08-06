import gevent


def test(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep()  # 休眠0, 主动切换执行权到其他Greenlet ~ (如果不切换, 会看到各Greenlet按阻塞顺序执行: 没有并发效果)
        # seconds: 休眠时间
        #   1.默认值0, 意味着切换执行权到任何其他可运行的greenlets, 但在事件循环周期前, 该greenlet可能会被再次调度 ~ 切换
        #       1.极端情况下, greenlet反复休眠0, 可以阻止一小段时间准备I/O的greenlets被调度
        #   2.seconds>0会延迟执行该greenlet, 直到该循环的下一次迭代
        # ref: 布尔值, 决定执行sleep()的greenlet是否阻止gevent.wait()退出


# g1 = gevent.Greenlet(test, 5)    # 创建Greenlet实例对象
# g2 = gevent.Greenlet(test, 50000)
# g3 = gevent.Greenlet(test, 5)
# g1.start()    # 调度gevent在循环迭代中执行
# g2.start()
# g3.start()
g1 = gevent.spawn(test, 5)    # 创建Greenlet实例对象, 并调度该对象去执行test函数
g2 = gevent.spawn(test, 50)
g3 = gevent.spawn(test, 5)

g1.join()    # 阻塞直到Greenlet结束, 或timeout到期, 无论如何都返回None
g2.join()
g3.join()


# 参考
#   1.PyPI: https://pypi.org/project/greenlet/
#     1.文档: http: // www.gevent.org

# gevent是一个基于协程的网络库, 在libev或libuv event loop之上, 使用greenlet提供高级同步API























