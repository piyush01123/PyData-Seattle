from time import sleep

def add1(x, y):
    return x + y

class Adder:
    def __call__(self, x, y):
        return x + y

add2 = Adder()

print(add1(5, 10))
print(add2(5, 10))


## creating stateful functions
class AdderNew:
    def __init__(self):
        self.z=0
    def __call__(self, x, y ):
        self.z += 1
        return x + y + self.z

add3 = AdderNew()
print(add3(5, 10)) #16
print(add3(20, 30)) #52
print(add3(10, 10)) #23

def compute():
    rv = []
    for i in range(10):
        sleep(0.5)
        rv.append(i)
