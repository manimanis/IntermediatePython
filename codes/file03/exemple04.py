# file03/exemple04.py
class CustRange:
    def __init__(self, start, end, step=1) -> None:
        self._start = start
        self._end = end
        self._step = step
    
    def __iter__(self):
        self._cur = self._start
        return self
    
    def __next__(self):
        if self._cur * self._step > self._end * self._step:
            raise StopIteration
        else:
            val = self._cur
            self._cur += self._step
            return val
        
# file03/exemple04.py
from random import randint

x = randint(1, 6)
if x in CustRange(1, 6, 2):
    print(x, "est impair")
else:
    print(x, "est pair")

s1 = set(CustRange(1,9)) - set(CustRange(2, 9, 3))
print(s1) # {1, 3, 4, 6, 7, 9}