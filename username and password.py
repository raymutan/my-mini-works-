import re
import colorama
from colorama import Fore
def invalid():
 print(Fore.RED  + 'Password must contain characters from two of the following four categories: Uppercase characters A-Z  Lowercase characters a-z Digits 0-9. Special characters (!, $, #, %, etc.)')

 
def passcheck(password):
    if (len(password)<8):
     invalid()
    elif not re.search("[a-z]", password):
     invalid()
    elif not re.search("[A-Z]", password):
      invalid()
    elif not re.search("[0-9]", password):
      invalid()
    elif not re.search("[!$%#]" , password):
      invalid()
    else:
      print('password successfully created!')
      

 #emulate terminal as outer console
from getpass import getpass
print('sign up today')

name1 = (input('your username will be '))
pass1 =(input('your password is '))
passcheck(pass1)

userpass=(input('username:'))
if (userpass!= name1):
    print('wrong username')
    quit()
else:
    passpass = (getpass('password: '))
if (passpass!=pass1):
    print('wrong password')



                  
























