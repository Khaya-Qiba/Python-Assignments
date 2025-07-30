# Python-Assignments
Assignmnet 1: OOP Assignment
# 🦸 Superhero Class in Python

## Overview
This assignment introduces Object-Oriented Programming (OOP) in Python through the design of a `Superhero` class. The class uses constructors, attributes, methods, **encapsulation**, and **inheritance** to simulate realistic character behaviors and relationships.

## Features
- Define a base class `Superhero` with core attributes.
- Use a constructor `__init__()` to initialize unique values.
- Encapsulate sensitive data using private variables.
- Extend functionality with a child class `FlyingHero`.
- Override methods using inheritance to demonstrate polymorphism.

## Code Highlights
```python
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.__origin = origin


