# -*- coding: utf-8 -*-
# print(abs(-12))
# b=min(-1,29,7)
# print(b)
# print(int(23.4))
# print(float('23.4'))
# print(str(12.354))
# print(bool(1))
# print(bool(None))
# print(str(123))
# 定义函数
# def my_abs(x):
#     if x>0:
#      return x
#     else:
#      return -x

# print(my_abs(-99))
# def nop():
#     pass
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad oprand type')
#     if x>0:
#         return x
#     else:
#         return -x

# my_abs('A')
#默认参数
# def power(x=5,n=2):
#     s=1
#     while n>0:       
#         s=x*s
#         n=n-1
#     return s
# print(power(n=3))
#可变参数
# def calc(*numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# print(calc(*(2,3)))
#关键字参数
# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
# person('Roin',20)
# person('Roin',20,city='Shanghai',gender='F')
# person('Roin',20,**{'city':'上海','gender':'F'})
#命名关键字参数
# def person(name,age,**kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:',name,'age:',age,kw)
# person('Robin',20,zh='hhh')
# def person(name,age,*,city,job):
#     print(name,age,city,job)
# person('Robin',20,job='工程师',city="江苏")
# person('Robin',20,city="江苏",job='工程师')
# person('Jack', 24, city='江苏', job='工程师')
# def person(name,age,*numbers,job,city):
#     arg=' '
#     for number in numbers:
#         arg=arg+number+arg
#     print(name,age,arg,city,job)
# person('Robin',20,*['中国','o型血'],city='江苏',job='工程师')
#递归函数
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(1000))