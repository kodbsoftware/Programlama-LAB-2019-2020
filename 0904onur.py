Created on Thu Apr  9 16:21:37 2020

@author: onur


x=1
p=x*(x+x)
print(p)
p=(x+2)*(x+3)
print(p)
from sympy import Symbol
y=Symbol('y')
from sympy import factor
expr=x**2-y**2
factors=factor(expr)
expand=expand(factors)
print(factors,expand)
expr=x**3+3*x**2*y+3*x*y**2+y**3
factors=factor(expr)
print(factors)
from sympy import pprint
pprint(factors)
x=Symbol('x')
series=x
n=5
for i in range(2,n+1):
    series=series+(x**i)/i
print(series)
expr=x*x+x*y+x*y+y*y
res=expr.subs({x:1, y:2})
print(res)
r=expr.subs({x:1-y})
print(r)

x=Symbol('x')
series=x
n=5
for i in range(2,n+1):
    series=series+(x**i)/i
print(series)
series_value=series.subs({x:x_value})
print(series_value)
