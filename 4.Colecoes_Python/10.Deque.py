"""
Deque é uma lista de alta performance
"""
from collections import deque
deq = deque('geek')
print(deq)
print('\nAdicionando elementos na lista')
deq.append('y')
print(deq)
print('\nesquerda')
deq.appendleft('k')
print(deq)
print('\nremover')
print(deq.pop())
print(deq)
print('\nremover 1 elemento')
print(deq.popleft())
print(deq)