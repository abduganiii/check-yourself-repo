# магические методы - это в первую очередь те методы которые имеют __ __, срабатывают они при выполнении операции ><-.==+/**%
# dunder methods - double underscore methods

# new - это конструктор класса, отвечает за создание класса
# init - инициализатор класса, задает созданному объекту аттребуты
# del - деструктор класса, отвечает за удаление объекта

#class User:


   # def __new__(cls, *args, **kwargs):
   #     print('new worked: ')
   #     return super().__new__(cls)
    
  #  def __init(self, name, email) -> None:
  #      print('init worked: ')
  #      self.name = name
  #      self.email = email

 #   def __del__(self):
 #       print('del worked: ')
#user = User('Nikita', 'nikita@gmail.com')


class Myint(int):
    def __init__(self, value) -> None:
        self.value = value

    def __add__(self, other: int) -> int:
        return f'этосложение и результат равен:{self.value + other}'
# ** - __pow__
# % - __mod__
# > - __lt__
obj_int = Myint(5)
print(obj_int+9)


# в чем отличие методов с буквой г в нвчале и 

#class MyInt(int):
 #   def __init__(self, value) -> None:
 #       self.value = value

 #   def __lt__(self, __value: int) -> bool:
 #       return self.value > __value
    
 #   def __gt__(self, __value>__value)


# __getitem
#a = 'asdf'
#a = [0]
#dict












