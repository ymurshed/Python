class Methods:
  def i_method(self,x):
    print(self,x)

  @staticmethod
  def s_method(x):
    print(x)

  @classmethod
  def c_method(cls,x):
    print(cls,x)

if __name__ == 'main':
    obj = Methods()
    
    obj.i_method(1)
    Methods.i_method(obj, 2)
    
    obj.s_method(3)
    Methods.s_method(4)
    
    obj.c_method(5)
    Methods.c_method(6)