#!/Users/vadlakun/.pyenv/shims/python
import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class Singleton(metaclass=Cached):
    def __init__(self, val):
        print(f"Creating Singleton({val})")
        self.val = val


if __name__ == '__main__':

    obj1 = Singleton("Helloo")
    print(id(obj1))

    # A new object would be created
    obj2 = Singleton("Different Hello")
    print(id(obj2))

    # Here cached obj1 id would be returned since the same arg is passed
    obj3 = Singleton("Helloo")
    print(id(obj3))


