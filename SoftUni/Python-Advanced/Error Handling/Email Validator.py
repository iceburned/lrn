from custom_exceptions import *  # Empty classes for exceptional errors

"""
input:
peter@gmail.com
petergmail.com
"""

data = input()
domains = (".com", ".bg", ".net", ".org")  # container for domains

while not data == "End":  # in input examples there is no End, but from description should be in code

    if '@' not in data:
        raise MustContainAtSymbolError("Email must contain @")          # MustContainAtSymbolError

    name, domain_part = data.split("@")

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")  # NameTooShortError

    # comment this, before uncomment code bellow and vise versa
    flag = any([True for _ in domains if domain_part.endswith(_)])  # check for present domain with dot
    # flag = False
    # for _ in domains:
    #     if domain_part.endswith(_):           # same without list comprehension
    #         flag = True

    if not flag:                                                         # InvalidDomainError
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    data = input()

"""
output:
Email is valid
Traceback (most recent call last):
  File ".\email_validator.py", line 18, in <module>
    raise MustContainAtSymbolError("Email must contain @")
__main__.MustContainAtSymbolError: Email must contain @
"""