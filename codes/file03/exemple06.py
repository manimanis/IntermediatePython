# file03/exemple06.py
class FiboSequence:
    def __init__(self, end) -> None:
        self._end = end
        self._u0 = 1
        self._u1 = 1
    
    def __iter__(self):
        self._un = 1
        self._i = 0
        return self
    
    def __next__(self):
        if self._un > self._end:
            raise StopIteration
        val = self._un
        self._i += 1
        if self._i < 2:
            self._un = 1
        else:
            self._un = self._u0 + self._u1
            self._u0 = self._u1
            self._u1 = self._un
        return val

for i in FiboSequence(100):
    print(i, end=", ")
print()
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
