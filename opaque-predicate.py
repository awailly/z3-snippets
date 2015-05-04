from z3 import *

esp, esp1, esp2 = BitVecs('esp esp1 esp2', 32)
eax = BitVec('eax', 32)

s = Solver()
s.add(esp1 == esp & 0x0FFFFFFF0)
s.add(esp2 == esp1 - 0x10)
s.add(eax == 0xf)
s.add(eax == esp2)
print s.check()
print s.model()
