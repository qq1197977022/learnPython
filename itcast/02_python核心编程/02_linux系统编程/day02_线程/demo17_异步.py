# 一.同步和异步: 关注消息通信机制
#   1.同步: 发出调用后, 得不到结果前调用不返回 ~ 调用者主动等待调用结果
#   2异步: 发出调用后, 该调用直接返回, 调用者不会立刻得到结果,\; 被调者通过状态/通知来告知调用者, 通过回调函数处理调用结果


# 二.阻塞和非阻塞: 关注程序等待调用结果(消息/返回值)时的状态
#   1.阻塞: 调用结果返回前, 当前线程被挂起, 直到得到结果后才返回
#   2.非阻塞: 调用结果返回前, 该调用不会阻塞当前线程
















