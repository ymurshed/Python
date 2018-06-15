from abc import ABC, abstractmethod
from interface import Interface, implements

#Abstract class
class AreaAbstract(ABC):
    __h, __w, area = 0, 0, 0
    
    def __init__(self, h, w):
        self.__h = h
        self.__w = w
        
    def calc_area(self):
        self.area = self.__h * self.__w # area of rectangle

    @abstractmethod
    def show_area(self):
        pass 
    
#Abstract class implementation
class MyAbstract(AreaAbstract):
    def __init__(self, h, w):
        return super().__init__(h, w)
    
    #Override implementation
    def show_area(self):
        print('Area = ' + str(self.area))
    
#Interface
class SquareInterface(Interface):
    def calc_square(self, arg1):
        pass

    def show_square(self):
        pass
    
# Interface implementation    
class MyInterface(implements(SquareInterface)):
    def calc_square(self, arg1):
        self.__result = arg1 ** 2 # square of arg1
        
    def show_square(self):
        print('Square = ' + str(self.__result))
    
try:
    ob1 = MyAbstract(5, 6)
    ob1.calc_area()
    ob1.show_area()
    
    ob = MyInterface()
    ob.calc_square(10)
    ob.show_square()
    
except Exception as e:
    print(e)    