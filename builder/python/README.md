# Builder

* This is a creational design pattern. 
* In this design pattern, a builder class builds the final object in step-by-step procedure. This builder is independent of other objects.


## Director
* Director uses a concrete builder that implements the Builder interface.

## Builder Interface
* Builder interface that has the methods that get implemented by the concrete builder. This has the methods to create the product

## Concrete Builder
* Class that implements the Builder interface

## Product
* The product that gets created by the methods in the builder interface.

* It provides clear separation and a unique layer between construction and representation of a specified object created by class.


## Process

### Director makes use of a Builder to build a Product

* Director gets an instance of builder which has the getters for the product. 
* Director initializes the product object that has the setters.
* Director uses the getters to get details and set those details in the product
