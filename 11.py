# Дана функция f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

from sympy import solve, plot, diff, symbols, sin, cos 

print('Дана функция -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30')
x = symbols('x')
func = -12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30
ans = diff(func, x)

print(f'Корни уравнения: {solve (func, x)}')
print(f'Промежутки, на которых f > 0: {solve (func > 0, x)}')
print(f'Промежутки, на которых f < 0: {solve (func < 0, x)}')
print(f'Вершина ф-ии: {solve (ans)}')
print(f'Промежутки, на которых ф-я возрастает: {solve (ans>0)}')
print(f'Промежутки, на которых ф-я убывает: {solve (ans<0)}')
print(plot(func)) #график

