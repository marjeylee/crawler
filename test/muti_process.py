import time
import random
from multiprocessing import Process


class Piao(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s piaoing' % self.name)
        i = 1
        while True:
            i = i + 1


if __name__ == '__main__':
    p1 = Piao('e')
    p2 = Piao('a')
    p3 = Piao('w')
    p4 = Piao('y')
    p1.start()  # start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    print('主线程')
