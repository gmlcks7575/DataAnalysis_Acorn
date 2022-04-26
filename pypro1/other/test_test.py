from abc import *

class Employee(metclass = ABCMeta):
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        pass
    
class Temporary(Employee):
    irum=''; nai=0; ilsu=0; ildang=0
    
    def irumnai_print(self,irum,nai,ilsu,ildang):
        Employee.irumnai_print(self)


t=Temporary('홍기동',25,20,15000)
t.data_print()