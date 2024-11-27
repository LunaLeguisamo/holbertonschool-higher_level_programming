#!/usr/bin/python3
from abc import ABC, abstractmethod
import math
# class Car:
    
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model 
#         self.year = year
        
#     def display_info(self):
#         print(self.brand)
        

# carcito = Car("toyota", "pepe", "1000")

# class Animal(ABC):
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
    
#     @abstractmethod
#     def make_sound(self):
#         print("some generic sound")
        
# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name
        
#     def make_sound(self):
#         print("Woof!")

# doggy = Dog("pepe")
# doggy.make_sound()

class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        if balance:
         self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            
    def get_balance(self):
        return self.__balance
    
acc = BankAccount(1000)
acc.deposit(100)
acc.withdraw(300)
acc.get_balance()
print(f"{acc.balance}")

class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Circle(Shape):
    def __init__(self, radio:int):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
class Rectangle(Shape):
    def __init__(self, largo:int, ancho:int):
        self.largo = largo
        self.ancho = ancho
        
    def area(self):
        return self.largo * self.ancho
    
circulo = Circle(2)
rect = Rectangle(23,56)
print(f"{circulo.area()}")
print(f"{rect.area()}")
