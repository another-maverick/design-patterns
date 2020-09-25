# Factory Method

* It is a creational design pattern
* If implementation of an interface depends on a parameter, instead of using if/elif/else, application delegates the job to a separate component that creates the object
* Application becomes simpler and much easier to maintain

* Factory Method should be used in every situation where an application (client) depends on an interface (product) to perform a task and there are multiple concrete implementations of that interface. You need to provide a parameter that can identify the concrete implementation and use it in the creator to decide the concrete implementation.
* Complex logical structures in the format if/elif/else are hard to maintain because new logical paths are needed as requirements change.


There are 3 components

## Client
* This is the entry point that helps the user carry out tasks
* This makes use of the "Creator" to get the right implementation

## Creator
* This takes some input from the client and makes a determination which implementation should be used

## Concrete Implementation(product)
* This is the actual concrete implementation.
 
 