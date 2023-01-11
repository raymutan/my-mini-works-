import re 

def passcheck(password):
    if (len(password)<8):
        print('Password must contain characters from two of the following four categories: Uppercase characters A-Z  Lowercase characters a-z  Digits 0-9. Special characters (!, $, #, %, etc.)')
    elif not re.search("[a-z]", password):
      print('Password must contain characters from two of the following four categories: Uppercase characters A-Z  Lowercase characters a-z  Digits 0-9. Special characters (!, $, #, %, etc.) ')
    elif not re.search("[A-Z]", password):
      print('Password must contain characters from two of the following four categories: Uppercase characters A-Z  Lowercase characters a-z  Digits 0-9. Special characters (!, $, #, %, etc.)')
    elif not re.search("[0-9]", password):
      print('Password must contain characters from two of the following four categories: Uppercase characters A-Z  Lowercase characters a-z  Digits 0-9. Special characters (!, $, #, %, etc.)')
    elif not re.search("[!@$%&*]" , password):
       print('Password must contain characters from two of the following four categories: Uppercase characters A-Z  Lowercase characters a-z Digits 0-9. Special characters (!, $, #, %, etc.)')
       
    else:
      print('password successfully created!')


passcheck(input('password is'))








