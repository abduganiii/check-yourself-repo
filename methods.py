"существует 3 вида методов"
# instance method 
# class method
#static method

class A:
    def instance_method(self):
        print('метод объекта')
        print(f'первый аргумент {self}')

obj = A()
obj.instance_method() # если вызываем у объекта, то self передается автоматически
A.instance_method(obj) # еслти вызваем у класса, то self нужно передать объект этого класса 

# instance method  - обычные методы, которые первым аргументом принимают self (ссылка на объект) они нужны для работы с аттребутами объекта

class B:
    @classmethod
    def class_method(cls):
        print('метод класса')
        print(f'первый аргумент класса')

obj = B()
obj.class_method()
B.class_method()
# не важно откуда мы вызываем classmethod gthdsv аргументом всегда прилетает ссылка на класс

# class methods - методы класса, которые принимают первым аргументом cls (ссылку на класс), нужны они для изменения аттрибутов и создания объектов, что бы создать класс метод мы должны задекорировать его classmethod
class C:
    def static_method(a, b):
        print('статичный метод')
        print('не принимает ни self ниcls (принимает то что нужно)')

import math
class Cylinder:
    def __init__(self, diametr, hight) -> None:
        self.diametr = diametr
        self.hight = hight
        self.area = self.get_area(diametr, hight)
        
   # @staticmethod
   # def get_area(d, h):
    #    return pi * 

#class Iphone15:
#    def __init__(self, name, cost) -> None
 #       self.name = name
 #       self.cost = cost

  #  @classmethod
  #  def change_cost(cls, new_cost):
  #      print(new_cost)
  #      return cls.cost 
    


#static method - просто функции внутри класса, которые не взаимодейсьтвуют ни с классом, ни с объектом, 
# они находятся внутри класса , что бы содать статичный метод егонужно задекорировать ststicmethod




        
