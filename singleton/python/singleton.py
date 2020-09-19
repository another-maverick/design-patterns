#!/Users/vadlakun/.pyenv/shims/python


class Singleton:

    class __inner:
        """
        An inner class that implements singleton.
        """
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    single_instance = None

    def __init__(self, arg):
        if not Singleton.single_instance:
            Singleton.single_instance = Singleton.__inner(arg)
        else:
            Singleton.single_instance.val = arg

    def __getattr__(self, arg):
        return getattr(self.single_instance, arg)


if __name__ == '__main__':

    obj1 = Singleton("First Hello")
    print(obj1)
    print(obj1.val)

    obj2 = Singleton("Second Hello")
    print(obj2)
    print(obj2.val)

    obj3 = Singleton("Third Hello")
    print(obj3)
    print(obj3.val)

    print(obj1.val)
    print(obj2.val)


    print(id(obj1))
    print(id( obj2))
    print(id( obj3))

