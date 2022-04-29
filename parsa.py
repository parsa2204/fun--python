class Car:

    number=0

    def __init__(self,name,lname,IDcode,car):
        self.name=name
        self.lname=lname
        self.IDcode=IDcode-
        self.mode=car
        self.color="white"
        Car.number += 1

    def choose_color(self,color):
        self.color=color

parsa=Car('parsa','sarkhosh','19','BMW')
print(parsa)