#!/Users/vadlakun/.pyenv/shims/python


class NewClass:
    """
    This is the New class.
    """

    def request(self):
        return(f"------- This is the target output -------")


class Legacy:
    """
    this is the legacy class.
    """

    def some_request(self):
        return(f"------- tuptuo tegrat eht si sihT -------")


class Adapter(NewClass, Legacy):
    """
    This is the adapter.

    can take client requests and convert to legacy or newclass

    support all classes that implement the target interface
    """

    def request(self):
        return(f"I am the adapter. If someone needs to pass the legacy object instead of newClass object somewhere, they can pass me. I can work as a proxy for legacy\n"
               f"Legacy Code: {self.some_request()[::-1]}")


def client_code(newclass_obj):
    """
    This is the client code that receives the new_class an input.
    if we need to pass legacy pbject here, we can pass adapter instead which does the conversion

    :param new_class: instance of the New Class
    :return:
    """

    print(f"Input object can be new_class object or legacy object. The new class request method will being called")
    print(f"INPUT OBJECT: {newclass_obj.__class__}")
    print(newclass_obj.request())


if __name__ == '__main__':
    """
    This is the client code.
    """

    # New CLass
    new_class = NewClass()

    # Client code using the new class
    client_code(new_class)

    print(f"########################")
    # Legacy default behavior
    legacy = Legacy()
    print(legacy.some_request())


    print(f"########################")
    # Pass adapter to the client code instead. This is indirectly making sure legacy is used by the client.
    adapter = Adapter()
    client_code(adapter)






