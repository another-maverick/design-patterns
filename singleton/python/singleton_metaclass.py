#!/Users/vadlakun/.pyenv/shims/python
import weakref


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class MyClass(metaclass=Singleton):
    def __init__(self, val):
        print(f"Creating MyClass({val})")
        self.val = val


if __name__ == '__main__':

    obj1 = MyClass("Helloo")
    print(id(obj1))

    # obj1 object would be returned
    obj2 = MyClass("Different Hello")
    print(id(obj2))

    # obj1 object would be returned
    obj3 = MyClass("Helloo")
    print(id(obj3))