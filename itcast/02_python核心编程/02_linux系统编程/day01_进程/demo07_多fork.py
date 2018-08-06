import os
os.fork()
os.fork()
os.fork()
print('.'*30)


# 类似细菌分裂: 进程数 = 2 ** n

# fork炸弹
#   while True:
#     os.fork()
