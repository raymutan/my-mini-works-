num=(int(input('ur number is ')))
def primecheck(num):
  flag=False
  num1=num
  if (num==1)or(num1==0):
    print('invalid')
  else:
    print('stage2')
    for i in range(2,num1):
      if (num1%i==0):
        print('{} not a prime no.'.format(num1))
        break
    else:
        print('{} is a prime no.'.format(num1))
        
primecheck(num)        
