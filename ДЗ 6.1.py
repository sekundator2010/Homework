import time
from itertools import cycle
class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']
    def running(self):
        for i in cycle(self.__color):
            yield i

traf1 = TrafficLight()
for coloring in traf1.running():
    print(coloring)
    if coloring == 'red':
        time.sleep(7)
    elif coloring == 'yellow':
        time.sleep(2)
    elif coloring == 'green':
        time.sleep(5)





