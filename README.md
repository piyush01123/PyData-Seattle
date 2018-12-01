
I wrote all this while watching this PyData conference <https://www.youtube.com/watch?v=cKPlPJyQrt4>


`dunder` stands for double underscore functions. This shows creating python  ops for custom objects like `+`, `print` and so on.


`stars.py` is not actually covered in conference. Wrote this to play with `*args` and `*kwargs` arguments of functions used to pass arguments to functions arbitrarily. `*args` lets you write `f(0,1,2)` without `f` asking for three arguments and `*kwargs` lets you write `f(x=0,y=1,z=2)` without f asking for x, y or z. args get passed to function as list and kwargs as dict.


In `decorators`, `@dec` is fancy for dec(f) where f is a function. You also get to write @(dec(n))


In `gen.py`, I have shown
- stateful  functions. What if you need a function that has to change its definition everytime it is called? You write a stateful function.
- Generators - What if you have a function that takes a lot of time to do something (say load data from a db)


Lets say your org. has a core library with Base class and a user code with Derived class. If you are in user team and want to verify library methods its simple ie you write test, or use assert(hasattr)
What if you are in the core library team and need something written by user team? Answer is something called Metaclass.
You add a `BaseMeta` class as the "metaclass" for your `Base` class and inside the method that gets executed while this `BaseMeta` class is being built (not instantiated) that is the `__new__` method you check that the method that you need from user library exists.
