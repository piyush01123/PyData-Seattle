class Polynomial:
    def __init__(self, *coefs):
        self.coefs = coefs
    def __repr__(self):
        return 'Polynomial {!r}'.format(self.coefs)
    def __add__(self, other):
        return Polynomial(*(x+y for x, y in zip(self.coefs, other.coefs)))
    def __len__(self):
        return len(self.coefs)
    def __call__(self):
        pass

p1 = Polynomial(5,3,2) #5x^2 + 3x + 2
p2 = Polynomial(7, -1, 0) #7x^2 - x
p3 =  p1 + p2
print(p3)
