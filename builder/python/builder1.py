#!/Users/vadlakun/.pyenv/shims/python



#Product

class Car:
    def __init__(self):
        self.__wheels = []
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def set_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print(f"body - {self.__body.shape}")
        print(f"wheel size - {self.__wheels[0].size}")
        print(f"Engine - {self.__engine.power}")


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.set_wheel(wheel)
            i += 1

        return car


class Builder:
    """
    The builder interface. Has all the methods for creating the product.

    """

    def get_wheel(self):
        pass

    def get_engine(self):
        pass

    def get_body(self):
        pass


class SuvBuilder(Builder):
    """
    Concrete implementation of the Builder.

    """

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 21
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.power = 350
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body


class Wheel:
    size = None

class Engine:
    power = None

class Body:
    shape = None


if __name__ == '__main__':
    suv_builder = SuvBuilder()

    director = Director()

    director.set_builder(suv_builder)

    suv = director.get_car()

    suv.specification()



