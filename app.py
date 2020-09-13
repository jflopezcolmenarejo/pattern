from dataclasses import dataclass

@dataclass
class OrderLine:
    order_id: str
    sku: str
    qty: int

my_order = OrderLine('12asd', 'ni-en-pedo', 78)

def add(a, b):
    """Add function"""
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    """Multiply function"""
    return a * b

def divide(a, b):
    """Divide function"""
    if b == 0:
        raise ValueError('cannot divide by zero')
    return a / b
