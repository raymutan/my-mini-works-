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
    elif not re.search("[_@$]" , password):
      invalid()
    else:
      print('password successfully created!')
      
passcheck(input('password is'))







