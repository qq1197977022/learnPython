import threading
import time


def fun():
    num = 100
    t_name = threading.current_thread().name
    if t_name == 'Thread-1':
        num += 1
    else:
        time.sleep(2)
    print(f'{t_name:->30}{num:->30}')


if __name__ == '__main__':
    t1 = threading.Thread(target=fun)
    t1.start()

    t2 = threading.Thread(target=fun)
    t2.start()

    print(f'{threading.current_thread().name:=>30}')









