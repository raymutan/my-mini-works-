def passcheck(password):
    if (len(password)<8):
        print('invalid')
    else:
        print('valid password')


passcheck(input('password is'))








