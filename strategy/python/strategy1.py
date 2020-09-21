#!/Users/vadlakun/.pyenv/shims/python

from __future__ import annotations
from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    Here we define all the methods that will be implemented by all the versions of the algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def common_func(self, data):
        pass


class ConcreteStrategy1(Strategy):
    """
    First implementation of the Strategy.

    """

    def common_func(self, data):
        """

        :param data: List
        :return: List
        """
        return sorted(data)


class ConcreteStrategy2(Strategy):
    """
    Second implementation of the Strategy.

    """

    def common_func(self, data):
        """

        :param data: list
        :return: list
        """
        return reversed(sorted(data))





class Context:
    """
    This implements the Strategy interface.

    This is an entry point to the concrete
    """

    def __init__(self, strategy_object):
        """
        Accepts the instance of Strategy method and updates it via a property.

        :param strategy_object: instance of Strategy implementation(ConcreteStrategy1 or ConcreteStrategy2)
        """

        # this is an internal instance variable that will be made a property.
        self._strategy_object = strategy_object


    @property
    def strategy_object(self):
        """
        Getter for the strategy object
        :return: instance of Strategy implementation(ConcreteStrategy1 or ConcreteStrategy2)
        """

        return self._strategy_object


    @strategy_object.setter
    def strategy_object(self, strategy_obj_val):
        """
        Setter for the stragey object.

        :param strategy_obj_val: instance of Strategy implementation(ConcreteStrategy1 or ConcreteStrategy2)
        :return: instance of Strategy implementation(ConcreteStrategy1 or ConcreteStrategy2)
        """

        self._strategy_object = strategy_obj_val


    def business_logic(self):
        """
        A method that has the business logic.
        Takes the strategy object as ain input and calls the common method.
        Then executes some common business logic.

        :return: None
        """

        print(f"I am the context. I am not sure which strategy object is passed to me. "
              f"I will just execute the object's method and then execute my own business logic")

        strategy_result = self._strategy_object.common_func(["a","c","b","e","d","f"])


        print(f"{'-'.join(strategy_result)}")



if __name__ == '__main__':

    # The client code picks a concrete strategy and passes it to the context.
    concrete_strategy1_obj1 = ConcreteStrategy1()
    print(f"Concrete strategy 1 object created. Passing to context now..")
    context_obj1 = Context(concrete_strategy1_obj1)

    # Then execute business logic of context which in turn executes the common func of strategy first
    print(f"{context_obj1.business_logic()}")


    # Repeat above for strategy 2
    # The client code picks a concrete strategy and passes it to the context.
    concrete_strategy1_obj2 = ConcreteStrategy2()
    print(f"Concrete strategy 2 object created. Passing to context now..")
    context_obj2 = Context( concrete_strategy1_obj2 )

    # Then execute business logic of context which in turn executes the common func of strategy first
    print(f"{context_obj2.business_logic()}")


