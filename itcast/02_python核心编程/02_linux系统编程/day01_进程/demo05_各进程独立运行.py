import os, time


def f1():	# 子进程先结束
	ret = os.fork()    # fork一个子进程

	if ret == 0:
		time.sleep(1)
		print('子进程结束...pid = {}'.format(os.getpid()))
	else:
		time.sleep(3)
		print('父进程结束...pid = {}'.format(os.getpid()))
	print(ret)



def f2():	# 父进程先结束
	ret = os.fork()

	if ret == 0:
		time.sleep(3)
		print('子进程结束...pid = {}'.format(os.getpid()))
	else:
		time.sleep(1)
		print('父进程结束...pid = {}'.format(os.getpid()))
	print(ret)


if __name__ == '__main__':
	print('当前集成pid = {}'.format(os.getpid()))
	f1()
	# f2()
	print('**'*30)

# 父子进程独立，但是只有父进程技术时才会出现命令提示符，因为父进程是主进程