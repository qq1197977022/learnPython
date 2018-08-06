import threading
import time


class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f'{self.name}\t{i}')


if __name__ == '__main__':
    for i in range(5):
        t = SubThread()
        t.start()








