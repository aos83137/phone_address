# def say_hello(name):
#     print('hello',name)
#
# def say_bye(name):
#     print('bye',name)
#
#
# say_hello('abcss')
# say_hello('ejejje')
# say_bye('def')
# def add(first,second):
#     print(first, '+', second, '=', first+second)
#
# add(1,2)
# add(10,20)
# add(second=5,first=2) #이름을 지정할 경우 순서 상관없음
#
# def bigger(num1,num2):
#     # if num1 > num2:
#     #     print(num1)
#     # else:
#     #     print(num2)
#     print(num1 if num1>num2 else num2)
#
# bigger(10,20)
#
# def hello2(age, name='user'):
#     print('hello',name, age)
#
# hello2(20)
# hello2(20,'abc')

# def print_tp(*t):  #*튜블
#     print(t)
#
# def print_dn(**d): #**딕셔너리
#     print(d)
#
# print_tp(1,2,3,4,5)
#
# print_dn(first=1, second=2, third=3)

# def sum_int(*n):
#     sum=0
#     for i in n:
#         if type(i) is int:
#             print(i,end=' ')
#             sum += i
#     print('다더하기!:',sum)
#
# sum_int(2,4,5,0.2,'42',True,123,4,51,24.2152,-2,24)

# def func(first, second):
#     print(first, second)
#
#
# param1 = [1, 2]
# param2 = [3, 4]
# dict = {"first":1, "second":2}
#
# func(*param1)
# func(*param2)
# func(*[5, 6])
#
# func(**dict)

# def avg_f(*n):
#     sum = 0
#     for i in n:
#         sum += i
#     avg = sum / len(n)
#     print('avg:', avg)
#
#
# avg_f(1, 2, 4, 6, 4, 5, 6)
#
#
# def avg2(*n):
#     sum = 0
#     cnt = 0
#     for i in n[1:-1:]:
#         sum += i
#         cnt += 1
#     avg = sum / cnt
#     print('avg:', avg)
#
#
# avg2(5, 4, 4, 12, 3, 4, 5, 5)
#
# def st_f(str):
#     result = True
#     for i in range(len(str)//2):
#         if str[i] != str[-(i+1)]:
#             result = False
#             break
#     print(result)
#
# st_f('토마토')

# def add(num1,num2):
#     return num1+ num2
#
# print(add(1,2))
# result = add(4,5)
# print(result)
#
# def add(num1, num2):
#     return num1 + num2
#     print('Hello')
#
# print(add(1,2))
# result = add(4,5)
# print(result)
#
# def single_int():
#     return 3
#
#
# def single_float():
#     return 5.5
#
#
# def list():
#     return [1, 2, 3]
#
#
# def set():
#     return {1, 2, 3}
#
#
# def tuple():
#     return 1, 2, 3
#
#
# def dictionary():
#     return {"a": 1, "b": 2, "c": 3}
#
#
# print(single_int(), type(single_int()))
# print(single_float(), type(single_float()))
# print(list(), type(list()))
# print(set(), type(set()))
# print(tuple(), type(tuple()))
# print(dictionary(), type(dictionary()))
#
# def list2(li):
#     min = li[0]
#     for i in range(1,len(li)):
#         if min > li[i]:
#             min = li[i]
#     return min
#
# print(list2([2,4,5,1,6,7,3,1231,12512,-231,-32635,12412]))

# def tuple():
#     return 1, 2, 3
#
#
# tp = tuple()
#
# print(tp, type(tp))
# x, y, z = tuple()
# print(x, y, z, type(x))
#
# x = 10
# x, _, z = tuple()
#
# def sumAndAvg(list):
#     sum = 0
#     for i in list:
#         sum += i
#     avg = sum / len(list)
#     return sum, avg
#
# list=[4,5,102,52,423,123,33,23]
# sum, avg = sumAndAvg(list)
# print('sum',sum)
# print('avg',avg)

# def min_max(list):
#     min = list[0]
#     max = list[0]
#
#     for i in list:
#         if max < i:
#             max = i
#         if min > i:
#             min = i
#     return max, min
#
# list=[5,3,6,2,-123,23,124,232351,12,-23241]
# mx, mn = min_max(list)
# print('max:',mx)
# print('min:',mn)
#
# sum =0
# def total(values):
#     global sum
#     for i in values:
#         sum +=i
#     print(sum)
# total([1,2,3])
# print(sum)
#
# def factorial(num):
#     result = 1
#     for i in range(num):
#         result *= (i+1)
#     return result
#
# def rc_factorail(num):
#     if num < 3:
#         return num
#     return num * rc_factorail(num-1)
# print(factorial(1))
# print(factorial(3))
# print(factorial(5))
# print(rc_factorail(3))
#
# def abs(value):
#     return [v if v>0 else -v for v in value]
#
# print(abs([1,2,3,-1,-2,-3]))
# print(abs(i for i in range(-3,3)))
# print((i for i in range(-3,3)))
# gen = (i for i in range(5))
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def my_gen(n):
#     for i in range(n):
#         yield i*10
#
#
# list = [i for i in my_gen(5)]
# print(list)
#
# def my_gen2(n):
#     for i in range(n):
#         yield i*20
#
# gen = my_gen2(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def my_range(*n):
#     step = 1
#     longs = len(n)
#     if longs == 1:
#         start = 0
#         end = n[0]
#     elif longs > 1:
#         start = n[0]
#         end = n[1]
#         if longs > 2:
#             step = n[2]
#
#     while start < end:
#         yield start
#         start += step
#
# list1 = [i for i in my_range(5)]
# list2 = [i for i in my_range(-5,20)]
# list3 = [i for i in my_range(-2,30,3)]
#
# print(list1)
# print(list2)
# print(list3)
#
# def add(n1, n2):
#     return n1 + n2
# def sub(n1, n2):
#     return n1 - n2
# def kake(n1, n2):
#     return n1 * n2
# def div(n1, n2):
#     if n2 != 0:
#         return n1 / n2
#     else:
#         return '0을 나눌수없다'
#
# func = {'+':add, '-':sub, '*':kake, '/':div}
#
# def executor(func, ob, n1, n2):
#     return func[ob](n1,n2)
#
# print(executor(func, '+', 166,2))
# print(executor(func, '-', 145,2))
# print(executor(func, '*', 12,2))
# print(executor(func, '/', 1,10))
#
# def add(n1, n2):
#     return n1 + n2
# def sub(n1, n2):
#     return n1 - n2
#
# def get_func(op):
#     if op == '+':
#         return add
#     elif op == '-':
#         return sub
#
# result = get_func('+')
# print(result(1,2))
# print(result(5,12))

# def calculate(op, n1, n2):
#     def add(n1, n2):
#         return n1+n2
#     def sub(n1, n2):
#         return n1-n2
#
#     if op== '+':
#         return add(n1,n2)
#     if op== '-':
#         return sub(n1,n2)
#
# print(calculate('+',5,19))
#
# def calculate(op):
#     def add(n1, n2):
#         return n1 + n2
#     def sub(n1, n2):
#         return n1 - n2
#
#     if op == '+':
#         return add
#     else:
#         return sub
#
# print(calculate('+')(5,123))

#
# def func():
#     value = 2
#     def nested_func():
#         nonlocal value
#         value = 3
#         print('nested', value)
#     nested_func()
#     print('outer', value)
#
# func()

# def func():
#     print('hello')
# func()
#
# def func():
#     print("bye")
# func()
#
# selection = int(input())
# if selection == 1:
#     def func():
#         print('hello')
# else:
#     def func():
#         print('byeeeeee')
# func()



# def add(n1,n2):
#     return n1+n2
# def sub(n1,n2):
#     return n1-n2
# def mul(n1,n2):
#     return n1*n2
# def div(n1,n2):
#     return n1/n2
# caculate_list = [add, sub, mul, div]
#
# u_num = int(input('입력 : '))
#
# if -1 < u_num < len(caculate_list):
#     result = caculate_list[u_num](10, 5)
# else:
#     result='없는 연산임'
# print(result)

stack = [1,2,3]
stack.append(4)
stack.append(5)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())

