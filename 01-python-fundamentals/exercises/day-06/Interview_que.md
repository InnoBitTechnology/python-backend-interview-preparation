What is a class?
a: A blue print to create the object

What is an object?
a: Intance of the class

What is the difference between a class and an instance?
a: 	A class is the blueprint, while an instance is an actual object created from that blueprint. A class can have multiple instances with different data.

What is __init__()?
a: 	A special method that initializes an object's attributes when an object is created. It is commonly called a constructor, though technically object creation and initialization are separate concepts in Python.

What does self represent?
a: current instance

What is an instance attribute?
a: 	An attribute that belongs to a specific object. Different objects can have different values.

What is a class attribute?
An attribute that belongs to the class and is shared by its instances unless overridden by an instance.

Difference between self and cls?
a: self belongs to the individul object, whereas cls refers to the class itself

What is @classmethod?
a: a method that receives the cls as it's first argument and can access/modify the class level data

What is @staticmethod?
a: a method that does not receive cls or self autometically, it behaves like normal function but is logically grouped inside the class

When would you use a static method?
a: when the functionality is the class related but does not need instance or class data.

What is encapsulation?
a: The practise of keeping the data and the method that operates on it together while controlling how the data is accessed.

What does _variable mean in Python?
a: it's private variable

What is name mangling?
a: Python changes the name of variables starting with __ to make accidental access or overriding harder.
self.__salary
# becomes internally:
self._Employee__salary

What is inheritance?
a: A child class gets properties and methods from a parent class.
class Dog(Animal):
pass
Dog IS-A Animal.

What is method overriding?
a: When a child class provides its own version of a parent method.

What does super() do?
a: It is used to call a method from the parent class.
super().__init__()

What is polymorphism?
a: Same method, different behavior depending on the object.

What is composition?
a: When one class contains an object of another class.
class Car:    
def __init__(self):        
self.engine = Engine()
Car HAS-A Engine.

Why might composition be preferred over inheritance in backend systems?
a: Because composition gives less coupling and more flexibility.
You can easily replace or test individual components without changing the whole class.

#helpfull note
'''
Inheritance  → IS-A
Composition  → HAS-A
Overriding   → Child changes parent method
super()      → Call parent method
Polymorphism → Same method, different behavior
'''