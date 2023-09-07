"""#what is abstract.
#An abstract class can be considered a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class.
from abc import ABC, abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self): # here the funtion name should be same in laptop class funtion
        pass
class laptop(computer):
    def process(self): # this funtion name should be same as computer class funtion(passing abstract method)
        print("running")
class whiteboard:
    def write(self):
        print("writing")
        
        
class programmer:
    def work(self,pro):
        print("checking bugs")
        pro.process()
com1 = laptop()
com2 = programmer()
com3 = whiteboard()
com2.work(com1)
com2.work(com1)"""

"""from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def func(self):
        pass   
   

    def func2(self):
        self.a  = 100
class B(A):
     def func(self,a):
        self.a = a
         

obj = B()
print(obj.func())
print(obj.func2())"""



from datetime import datetime
from datetime import timedelta
"""def time():
 x = date.today()
 z = x + timedelta(days = 7)
 return x-z"""



x  = open("c:\Users\Basavaraja\Pictures\open_file.txt", "r")
print(x)
#x = datetime.today()







    
