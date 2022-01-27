username = str(input())
password = str(input())
pass_ = str(input())
while pass_ != password:
    pass_ = str(input())
else:
    print('Welcome ' + username + '!')
