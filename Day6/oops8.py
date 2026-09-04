# Method resolution order(It's not intended for newbies)
class A:
    label = "A: Base class"

class B(A):
    label = "B: masla blend"

class C(A):
    label = "C: Herbal blend"

class D(B, C):
    pass

cup = D()
print(cup.label)      # it gives the B: Masala blend because we first write B.

# if we swipe the B and C
class D(C, B):
    pass

cup = D()
print(cup.label)     # it gives the C: Herbal blend.
print(D.__mro__)

# this __mro__ shows <class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>.
