import re 
flag=1
def invalid():
  print('Password must contain characters from two of the following four categories: Uppercase characters A-Z  Lowercase characters a-z Digits 0-9. Special characters (!, $, #, %, etc.)')
def passcheck(password):
    if (len(password)<8):
      invalid() 
    elif not re.search("[a-z]", password):
     invalid()
    elif not re.search("[A-Z]", password):
      invalid()  
    else:
      print('password successfully created!')
passcheck(input('password is'))







