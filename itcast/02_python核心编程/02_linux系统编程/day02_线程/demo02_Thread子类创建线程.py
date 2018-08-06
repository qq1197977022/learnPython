import threading
import time


class SubThread(threading.Thread):
    def run(self):
        print('Thread子类创建线程', self.name)
        time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        st = SubThread()
        st.start()




