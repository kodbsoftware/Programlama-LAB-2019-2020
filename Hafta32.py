from sympy import Finiteset

def probability(space,event):
    return len(event)/len(space)

def check_prime(number):
    if number!=1:
        for i in range(2,number):
            if number%i==0:
                return False
    else:
        return False
    return True

space =Finiteset(*range(1,21))
primes =[]
for num in space:
    if check_prime(num):
        primes.append(num)
event=Finiteset(*primes)
p=probability(space,event)
print(p)
