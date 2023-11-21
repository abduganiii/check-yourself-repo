# 1
class Cat:
    def voice(self):
        print('мяу-мяу')

class Dog:
    def voice(self):
        print('гав-гав')

objects = [Cat(), Dog()]

for i in objects:
    i.voice()

class A:
    def func(self):
        pass

class B(A):
    def func(self):
        pass


# 2
class Person:
    def __init__(self):
        self._name = None
        self._last_name = None
        self._age = None
        self._email = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

john = Person()

print(john.name)        
print(john.last_name)  
print(john.age)         
print(john.email)      

john.name = 'Abdugani'
john.last_name = 'Orunbaev'
john.age = 16
john.email = 'abduganiorunbaev@gmail.com'

print(john.name)       
print(john.last_name)  
print(john.age)        
print(john.email)       



# 1
from datetime import datetime

class CreateMixin:
    def create(self, key, todo):
        if key in self.todos:
            return "Задача под таким ключём уже существует"
        self.todos[key] = todo
        return f"Задача '{todo}' добавлена под ключом '{key}'"

class DeleteMixin:
    def delete(self, key):
        if key in self.todos:
            todo_name = self.todos.pop(key)
            return f"Удалили задачу '{todo_name}'"
        else:
            return "Задачи с таким ключом не существует"

class UpdateMixin:
    def update(self, key, new_value):
        if key in self.todos:
            self.todos[key] = new_value
            return f"Задача под ключом '{key}' обновлена"
        else:
            return "Задачи с таким ключом не существует"

class ReadMixin:
    def read(self):
        return sorted(self.todos.items())

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    def __init__(self):
        self.todos = {}

    def set_deadline(self, deadline):
        deadline_date = datetime.strptime(deadline, "%d/%m/%Y")
        current_date = datetime.now()
        days_left = (deadline_date - current_date).days
        return days_left

todo_list = ToDo()

print(todo_list.create("1", "Покормить кошку"))
print(todo_list.create("2", "Постирать белье"))
print(todo_list.update("1", "Покормить собаку"))
print(todo_list.read())
print(todo_list.delete("2"))
deadline_date = "31/12/2021"
days_left = todo_list.set_deadline(deadline_date)
print(f"Дней до дедлайна ({deadline_date}): {days_left}")

