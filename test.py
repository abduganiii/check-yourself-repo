# username
# email
# password
# password_confirm
# запись в бд
import re
{1:['username', '...'], 2:[]}

class RegisterUser:
    database = {}
    id = 1
    def __init__(self, username, email, password, password_confirm) -> None:
        self.id = RegisterUser.id
        RegisterUser.id+=1
        self.username = username
        self.email = email
        self.password = password
        self.password_confirm = password_confirm
        self.validate_password()
        self.database.update({self.id:[username, email, password]})
    
    def validate_password(self):
        symbols = '!@#$%^&*_+-~`'
        if not self.password == self.password_confirm:
            raise Exception('Пароли не совпадают')

        if len(self.password) <= 8:
            raise Exception('длина пароля должна превышать 8 символов')
        if not any(i.isalpha() for i in self.password):
            raise Exception('Пароль дожен состоять из букв')
        elif not any(i.isdigit() for i in self.password):
            raise Exception('Пароль дожен состоять из цифр')
        elif not any(i in symbols for i in self.password):
            raise Exception('Пароль дожен состоять из символов')

    def validate_email(self):
        if not re.match(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', self.email):
            raise Exception('не правильная почта')
        for v in self.database.values():
            if self.email in v:
                raise Exception('тфкая почта не существует')
    

# regex
# regular expression
# регулярные выражения

class LoginUserMixin:
    def login(self, email, password):
        for user_id, user_data in self.database.items():
            if user_data[1] == email and user_data[-1] == password:
                print('успешно залогинились')
                return {'id':user_id, 'username':user_data[0],'email':user_data[1]}
        print('')

#class User(RegisterUserMixin):
    database = {}

#user = User()

user = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
user1 = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
user2 = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
user3 = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')
user4 = RegisterUser('username', 'ff@gmail.com', '12345678!FFd', '12345678!FFd')

# написать validate_email, который будет проверять наличие сущ. email

# ToDo: CRUD - user
# listing
# retrieve
# update
# delete


    