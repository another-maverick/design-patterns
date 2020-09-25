#!/Users/vadlakun/.pyenv/shims/python

# Here we have a interface for the subject, implementation of the subject.
# Subject has a way of adding "observers" and "notify" them by calling their "update" method.
# Observers implement an observer interface that has the "update" method


from abc import ABC, abstractmethod
from random import randrange
import time

# Subject interface
class Subject(ABC):
    """
    This class is an interface for the subjects.
    """

    @abstractmethod
    def add(self, observer_obj):
        """
        Method to add an observer

        :param observer_obj: instance of the Observer
        :return: None
        """

        pass

    @abstractmethod
    def remove(self, observer_obj):
        """
        Method to remove an observer object from the list.

        :param observer_obj: instance of the Observer
        :return: None
        """

        pass

    @abstractmethod
    def notify(self):
        """
        notify all the observers
        :return: None
        """

        pass

#Implementation of the Subject

class ConcreteSubject(Subject):
    """
    This Subject implementation maintains a counter and notifies the subscribers when the counter changes
    """

    _counter = None

    # list of observers/subscribers

    _observers = []

    def add(self, observer_obj):
        """
        Adds an observer to the observer list

        :param observer_obj: instance of the Observer class
        :return: None
        """

        self._observers.append(observer_obj)

    def remove(self, observer_obj):
        """
        Removes an observer from the list.

        :param observer_obj: instance of the Observer class
        :return: None
        """

        self._observers.remove(observer_obj)


    def notify(self):
        """
        Notify all the observers.

        :return: None
        """

        print(f"notifying the observers")
        for each_observer in self._observers:
            each_observer.update(self)


    def business_logic(self):
        """
        Business logic that executes some code and creates the event that notifies the observers.

        :return: None
        """

        print(f"I am the subject and I am trying to execute some business logic.")
        self._counter = randrange(0,100)

        print(f"counter is now {self._counter}")

        print(f"notifying the observers now")
        self.notify()


# Observer interface
class Observer(ABC):
    """
    Interface for the observers.
    """

    @abstractmethod
    def update(self):
        """
        receives the subject object as input. Extracts the counter value from the subject's object
        :return:None
        """

        pass

# Concrete implementations for the Observer
class ConcreteObserver1(Observer):
    """
    First Concrete implementation of the observer.

    """

    def update(self, subject_obj):
        """
        receives the subject object as input. Extracts the counter value from the subject's object.
        This subject reacts when counter is less than equal to 40.

        :param subject_obj: instance of a Concrete Subject
        :return: None
        """

        if subject_obj._counter <= 40:
            print(f"I am Observer1. Received an event that matches my criteria")


class ConcreteObserver2(Observer):
    """
    Second Concrete implementation of the observer.

    """

    def update(self, subject_obj):
        """
        receives the subject object as input. Extracts the counter value from the subject's object.
        This subject reacts when counter is greater than 40.

        :param subject_obj: instance of a Concrete Subject
        :return: None
        """

        if subject_obj._counter > 40:
            print(f"I am Observer2. Received an event that matches my criteria")




if __name__ == '__main__':

    # Create an instance of the subject
    subject = ConcreteSubject()

    #Create an instance of the Observers. Add the observer to the subject
    #Observer1
    observer1_obj = ConcreteObserver1()
    subject.add(observer1_obj)

    #Observer2
    observer2_obj = ConcreteObserver2()
    subject.add(observer2_obj)


    # Execute subjects's business logic a few times just so we generate a few events
    for i in range(10):
        subject.business_logic()
        print(f"###################")
        time.sleep(2)











