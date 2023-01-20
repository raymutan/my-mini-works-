list=[]
def primecheck(num):
  num1=num
  if (num==1)or(num1==0):
    print('invalid')
  else:
    for i in range(2,num1):
      if (num1%i==0):
        break
    else:
        list.append(num1)
        print('{} is a prime number'.format(num1))
        

num=2
max_num=int(input('generate till:'))
while num<max_num:
  primecheck(num)
  num=num+1
  
total=len(list)
print('total no. of prime numbers = {}'.format(total))  
