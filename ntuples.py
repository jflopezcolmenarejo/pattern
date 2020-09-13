from collections import namedtuple
from typing import NamedTuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(11, y=22)
print(p[0]+p[1])

print(f'x = {p.x}')

class Bill(NamedTuple):
    """my bill class"""
    total_due_amount: int
    charges: int
    adjustments: int
    name: str

    def total(self):
        return self.charges - self.adjustments


bill1 = Bill(total_due_amount=10, charges=8, adjustments = 4, name='juan')
print(bill1)
print(bill1.charges)
print(bill1.total())

print(bill1._fields)
print(bill1.__class__.__name__)
print(type(bill1).__name__)