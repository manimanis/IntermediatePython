# file03/exemple05.py
class PrimeSequence:
    def __init__(self, end) -> None:
        self._end = end
    
    def __iter__(self):
        self._cur = 2
        return self
    
    def __next__(self):
        if self._cur > self._end:
            raise StopIteration
        val = self._cur
        self._cur = self.prem_suivant(val)
        return val

    def prem_suivant(self, n):
        i = n + (1 if n == 2 else 2)
        while True:
            prem = self.est_premier(i)
            if prem:
                break
            i += 2
        return i

    def est_premier(self, n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i, mx = 5, int(n**.5)+1
        while i <= mx:
            if n % i == 0:
                return False
            i += 2
        return True

for i in PrimeSequence(50):
    print(i, end=", ")
print()
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
