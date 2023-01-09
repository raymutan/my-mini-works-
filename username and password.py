#emulate terminal as outer console
from getpass import getpass
print('sign up today')
name1 = (input('your username will be '))
pass1 =(getpass('your password is '))
userpass=(input('username:'))
if (userpass!= name1):
    print('invalid username')
    quit()
else:
    passpass = (getpass('password: '))
if (passpass!=pass1):
    print('invalid password')
























