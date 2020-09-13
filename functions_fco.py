from typing import Callable

# The __call__ method enables Python programmers to write classes
# where the instances behave like functions and can be called like a function.

class Mersenne1:
    def __init__(self, algorithm: Callable[[int], int]) -> None:
        self.pow2 = algorithm
    def __call__(self, arg: int) -> int:
        return self.pow2(arg) - 1

def shifty(b: int) -> int:
    return 1 << b

def multy(b: int) -> int:
    if b == 0: return 1
    return 2*multy(b-1)

def faster(b:int) -> int:
    if b==0: return 1
    if b%2 == 1: return 2*faster(b-1)
    t = faster(b//2)
    return t*t

m1s = Mersenne1(shifty)
m1m = Mersenne1(multy)
m1f = Mersenne1(faster)

print(m1s(3))