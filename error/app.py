#IndexError 
friends = ["Alice", "Bob", "Charlie"]
# friends[3] # This will raise an IndexError because there is no index 3 in the list

#KeyError
friends = {'name': 'Alice', 'age': 25}
# friends['movie']

#nameError
# print(username)

#NotImplementedError
class User :
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def login(self):
        raise NotImplementedError("Subclasses must implement this method")

user = User("john_doe","password123")
# user.login()  # This will raise NotImplementedError

# 5+'hi' #TypeError

# int('20.5') #ValueError

#_________________Creating Youw Own Error in Python ______________________
class MyCustomError(TypeError):
    """
    Custom Error Class that extends TypeError
    """
    def __init__(self,message,code):
        super().__init__(f'Error Message : {message} | Error Code : {code}')
    # pass

# raise MyCustomError('my custom error occurred',404)
err = MyCustomError('another custom error',500)
print(err.__doc__)
raise err