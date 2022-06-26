class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
            return
        raise ValueError("The username must be between 5 and 15 characters.")

    @password.setter
    def password(self, value):
        is_length_valid = len(value) >= 8
        is_upper_present = any(True for _ in value if _.isupper())
        is_digit_present = any(True for _ in value if _.isdigit())
        if is_length_valid and is_upper_present and is_digit_present:
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password:' \
               f' { len(self.password) * "*"}'



