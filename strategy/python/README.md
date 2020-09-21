# Strategy pattern

* Grouping related algorithms under an abstraction, which allows switching out one algorithm or policy for another without modifying the client
* Provide users a way to change the behavior of a class without extending it
* Identification: Strategy pattern can be recognized by a method that lets nested object do the actual work, as well as the setter that allows replacing that object with a different one.
* Elements:

## Strategy(interface)
* The interface

## Concrete Strategy(interface implementation)
* Implements the interface in different fashions

## Context (business logic)
* Clients use this
* Client Code picks a concrete strategy and passes it to the context
* Based on what is passed, the context implementation varies


* Here the client picks a concrete strategy(algorithm) and passes it to the context.
* The Business logic would vary based on what is passed to teh context. 


