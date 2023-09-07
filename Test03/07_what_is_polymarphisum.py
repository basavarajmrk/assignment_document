#07:what is polymarphisum.
# In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.
x = len("string")
print(x)
y = len([1,8,6,5,4,2,3])
print(y)


name = "Ram"
age = 22
place = "bang"

message = "My name is {} and I am {} years {} and place of berth".format(name,age,place)
print(message)

#duck typing
# i have a code  to exicute but i need laptop so laptop is class(01)
class pycharm:
    def execute(self): # here pycharm has some funtion to execute code so need create eecute funtion and its behavier(03)
        print("compile")
        print("run")
class myide:  # here i am creating onther ide type myide and it has same method as pycharm(07)
    def execute(self):
        print("error")
        print("spell check")
        print("compile")
        print("run")

class laptop:
    def code (self,ide): # here i need to run my code i need ide so i need to get ide method from ide(pycharm) class(02)
        ide.execute() # here i got the execute method to run my code but we need to create object of ide to get the execute funtion(04)
lap = laptop() # here i need to create object of laptop(05)
ide = myide() # but we need to create object of ide to get the execute funtion(06)
#ide = myide()
lap.code(ide)# here i am passing prameter object ide into the code now the code is cmpliled and run using execute method

#operator overloding
class student:
    def __init__(self,m1,m2):
        self.m3 = m1
        self.m4 = m2
    def __add__(self, other):
        r1= self.m3 + other.m3     
        r2= self.m4 + other.m4 
        s3 = student(r1,r2)
        return s3
    def __gt__(self,other):
        r1 = self.m3 + self.m3
        r2 = other.m4 +other.m4
        if r1 > r2:

         return True
        else:
            return False
        

    
s1 = student(20,30)
s2 = student(50,40)
s3 = s1+s2
print(s3.m3) 
print(s3.m4)       

if s1 > s2:
    print("s1 win")
else:
    print("s2 win")






