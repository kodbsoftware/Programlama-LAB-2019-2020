Created on Thu Apr  9 19:19:24 2020

@author: onur
import sympy as sym
from sympy import Symbol
from sympy import pprint
%matplotlib notebook
import sympy.plotting as syp
sigma=Symbol('sigma')
x=Symbol('x')
mu=Symbol('mu')
part_1=1/(sym.sqrt(2*sym.pi*sigma**2))
part_2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))
my_gauss_function=part_1*part_2
pprint(my_gauss_function)
syp.plot(my_gauss_function.subs({mu:1,sigma:3}),(x,-10,10)title='gauss')


x_values=[]
y_values=[]
for value in range(-5,5):
    y=my_gauss_function.subs({mu:10,sigma:30,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)
%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(x_values,y_values)
plt.show()

print(sym.sqrt(2*sym.pi*sigma))
pprint(sym.sqrt(2*sym.pi*sigma)) 

gauss_function=1/(sympy.sqrt(2*sympy.pi*sigma))
gauss_function.subs({mu:0,sigma:1})
gauss_function

