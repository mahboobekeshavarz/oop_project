import helper.messages as msg

class WrongPasswordException(ValueError):
    def __str__(self):
        return msg.PASSWORD_LENGTH_ERROR

class TypePasswordException(TypeError):
    def __str__(self):
        return msg.PASSWORD_TYPE_ERROR

class WrongUsernameException(ValueError):
    def __str__(self):
        return msg.USERNAME_START_CHARACTER

class TypeUsernameException(TypeError):
    def __str__(self):
        return msg.USERNAME_TYPE_ERROR

class UsernameException(ValueError):
    def __str__(self):
        return msg.USERNAME_ADMIN_ERROR