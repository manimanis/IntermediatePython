# file03/exemple03.py
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
        

for i in CustRange(1, 6):
    print(i, end=", ")
print()
# 1, 2, 3, 4, 5, 6,

for i in CustRange(0, -8, -2):
    print(i, end=", ")
print()
# 0, -2, -4, -6, -8,


