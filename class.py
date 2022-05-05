import random
class Empoloyee:
    number= 0
    raise_of_salary=1.04
    def __init__(self , name ,lname , pay ):
        self.name=name
        self.lanme=lname
        self.pay=pay
        self.gmail=name+'.'+lname+"@gmail.com"
        self.idecode=random.randint(1000,100000)
        Empoloyee.number+=1

    def salary(self,y):
        self.money=3500000+y*40000
        return self.money

emp1=Empoloyee('Parsa','Sarkhosh',3500000)
print(emp1.salary(10))
