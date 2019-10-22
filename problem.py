# #1 - 해보기....
# rangth = int(input("길이를 입력하세요 : "))
# print("1. 센티미터를 인치로 변환")
# print("2. 인치를 센티미터로 변환")
# menu = int(input("입력 : "))
# result = 0
# if menu == 1:
#     result = rangth * 0.3937
# elif menu == 2:
#     result = rangth * 2.54
# print(result)

# 2
# num = int(input("num : "))
#
# if num == 0:
#     print("0")
# elif num == 1:
#     print("1")
# else:
#     arr = [0,1]
#     for i in range(2,num):
#         arr.append(arr[i-1] + arr[i-2])
#     print(arr)

# #3
# list=[123,92,87,134,112, 95, 78, 106, 109, 83]
# max, min = list[0], list[0]
# max_index, min_index = 0, 0
# for i in range(1,len(list)):
# #for i in list[1:]: #슬라이싱...
#     if max < list[i]:
#         max = list[i]
#         max_index = i
#     if min > list[i]:
#         min = list[i]
#         min_index = i
# print("Max :",max, max_index)
# print("Min :",min, min_index)
# # print("Max :",max(list))
# # print("Min :",min(list))

# 4

# str = input()
#
# for i in str:
#     n = int(i)
#     for j in range(n):
#         print('*', end='')
#     print()

# 5
# ===========내가한거
# nedan = int(input())
# oturi = 1000-nedan
#
# gohyaku, hyaku, gozyuu, zyuu = 0,0,0,0
#
# print(oturi)
#
# gohyaku = oturi//500
# hyaku = (oturi//100)%5
# gozyuu = (oturi//50)%2
# zyuu = (oturi//10)%10
#
# print("500원",gohyaku,"개 100원",hyaku,"개 50원", gozyuu,"개 10원", zyuu,"개")

# =============================================교수님꺼 쓴거
# price = int(input())
# change = 10000-price
#
# list = [1000,500,100,50,10]
# c = [0 for i in list]
#
# for i in list:
#     cnt = 0
#     while change >= int(i):
#         # print(i)
#         if change-int(i) >= 0:
#             change -= int(i)
#             cnt += 1
#         else:
#             break
#     c.append(cnt)
#     print(cnt)
# print(c)

# 6

# import random
#
# answer = random.randint(1, 100)
# cnt = 0
#
# while True:
#     user_num = int(input("숫자 입력: "))
#
#     if cnt == 9:
#         print("실패!~~ 기회 10번을 넘었어요 ㅠㅠ")
#         break;
#
#     if user_num == answer:
#         print("정답입니다~~!")
#         break
#     elif user_num > answer:
#         print("너무 큽니다.")
#     elif user_num < answer:
#         print("너무 작습니다.")
#
#     cnt += 1

# 7

# c = [0 for i in range(3)]
# list = [2000, 3000, 3500]
#
# menu = -1
#
# while True:
#     print("""
#     1.아메리카노\t\t2000
#     2.카페라떼\t\t3000
#     3.카페모카\t\t3500
#     0.주문끝내기
#     ---------------------
#     """)
#
#     menu = int(input("번호를 입력해주세요 : "))
#     if menu == 0:
#         break
#     c[menu - 1] += 1
#
# sum = 0
# for i in range(3):
#     sum += list[i] * c[i]
# print('------------------------------')
# print("아메리카노\t2000x", c[0], "=", 2000 * c[0]) if c[0] != 0 else 0
# print("카페라떼\t\t3000x", c[1], "=", 3000 * c[1]) if c[1] != 0 else 0
# print("카페모카\t\t3500x", c[2], "=", 3500 * c[2]) if c[2] != 0 else 0
# print("""------------------------------
# 합계 : %sum
# """ % sum)

# 8

# list = [1,7,3,8,5,9]
# temp = 0;
#
# length = len(list)
# for i in range(6):
#     flag = i
#     for j in range(i+1, 6):
#         if list[flag] > list[j]:
#             # temp = list[flag]
#             # list[flag] = list[j]
#             # list[j] = temp
#             list[flag],list[j] = list[j],list[flag]
#
# print(list)

# 9buble
# list=[55,7,78,12,42]
#
# length = len(list)
# # for i in length
# #
# #
# #
# # l

# def info(list):
#     sum = 0
#     for i in list:
#         sum+=i
#     avg = sum/len(list)
#     return sum, avg
#
# list = [1,2,3,4,5,6,7,8,9,10]
# sum, avg = info(list)
# print(sum, "\n", avg)

# def func(first, second):
#     first += 10
#     second.add(4)
#
# number = 1
# set={1,2, 3}
# func(number, set)
# print(number, set)

# list= [i for i in range(6)]
# print(list)
# print(list.index(2))
# list.insert(3, -1)
# print(list)
# list.append(6)
# print(list)
# list.extend([7,8,9])
# print(list)
# list.sort()
# print(list)
# list.reverse()
# print(list)

# list = [i for i in range(1,6)]
# list.insert(0,6)
# list.append(0)
# print(list)
# list.sort()
# print(list)
#
# list = [i for i in range(1,6)]
# del list[1]
# print(list)
# list.remove(1)
# print(list)
# list.remove(5)
# print(list)
#
# a,b = 1,2 #튜플 취급일듯
# print(type({1,2}))

# test = '안녕하세요 반갑습니다 ㅎㅎ!!!/실/험/용'
# arr  = test.split()
# arr2 = test.split('/')
# print(arr)
# print(arr2)
# arr3 = list(test) #한글자씩 리스트 만들어 버림
# print(arr3)
# arr4 = '$'.join(test)
# print(arr4)
#
# print(arr4[:10:2])
# print(arr3[3::])
# print(arr3[2:-2:])
# print(arr3[::2])


# list = [i for i in range(10)]
# print(list[-1])
# print(list[-3])
# print(list[:-3])
# print(list[-5:])

# print(list)
# del list[:3] #0,1,2 삭제
# print(list)
# del list[4:-1] #
# print(list)
#
# print(list)
# list[1:3] = [100, 200,1,2,3,4,5,6,7,8,9,0]
# print(list)
# list[1:-1] = [i for i in range(100, 1001, 100)]
# print(list)
#
# n = input()
# print(n[:3],n[-3:])
#
# capitals = {'korea':'Seoul', 'UK':'London'}
# days = {1:31, 2:28, 3:31, 4:30}
# print(capitals['korea'])
# print(days[1])
# days[50] = 31
# print(days)
# del capitals['UK']
# print(capitals)
# capitals.update({'yong':'seok', 'kojima':'yumeno'})
# print(capitals)

# set은 중복을 허용하지 않는 데이터의 모음 리스트,딕셔너리 빼고는 다 저장 가능
# set()함수 또는 {}를 사용함
# set1 = set([1,2,3,1.1,2.1,3.1,'Hello',1,1,1,1,1])
# set2 = {(1,2),3,4,'Hello',1,1,1,1,}
# print(set1); print(set2)

# passwd = input()
# var_len = len(passwd)
# if 4<= var_len <=10:
#     print('OK')
# else:
#     print('NG')

# age = 18
# print('Hello' if age>19 else 'too yong')
# print('Hello') if age > 19 else print('Too yong')
#
#
# v1 = int(input())
# v2 = int(input())
#
# print('OK' if v1+v2 >=0 else 'NG')
# print('OK') if v1+ v2 >=0 else print('NG')

# list = [i for i in range(10)]
#
# for i in list[3:]:
#     print(i)
#
#

# str = 'Hello everyone'
# for s in str:
#     if
#     print(s, end='.')
# str_join = '.'.join(str)
# print()
# print(str_join)

# for i in range(4):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# list_str = list('안녕하세요1234')
# for index, i in enumerate(list_str):
#     print(index, i)

# arr1 = [1,2,3,4,5]
# arr2 = [9,8,7,6,5]
# # arr3 = [i for i in range(10, 51, 10)]
# arr3 = [i*10 for i in range(1,6)]
# for i, j in zip(arr1, arr2):
#     print(i, j)
# for i, j , k in zip(arr1,arr2,arr3):
#     print(i,j,k)

# list_comprehension = [i*3 for i in range(1,11)]
# print(list_comprehension)
#
# arr =[i for i in range(100) if i%2==0]
# print(
#     arr
# )
#
# scores = [80,95,66,88,77,74,98,90]
# a_grade = [s for s in scores if s >=90]
# print(a_grade)

# arr = []
# for i in range(5):
#     arr.append(int(input()))
# arr2 = [i for i in arr if i>0]
# print(arr)
# print(arr2)
#
# set1 = {i for i in range(10)}
# print(set1)
# set2= {1,1,2,3,3,5,5,6,6,7}
# print(set2)

# list =[1,7,3,8,5,9]
#
# for i in range(len(list)):
#     flag = i
#     for j in range(i,len(list)):
#         if list[flag] > list[j]:
#             flag = j
#     if flag != j:
#         list[flag], list[i] = list[i], list[flag]
#
# print(list)

# 완벽


# list = [55, 7, 78, 12, 42]
# cnt = 0 # 버블 정렬시 list개수 만큼 pass가 일어나면 정렬이 끝나니까 pass의 count를 세아리면 간단
# while cnt < len(list):
#     for j in range(len(list)-1):
#         if list[j]>list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
#         else:
#             cnt +=1 #패스 카운터
#             pass
#
# print(list)

# for i in range(len(list)-1):
#     for j in range(0,len(list)-i-1):
#         if list[j] > list[j + 1]:
#                 list[j], list[j+1] = list[j+1], list[j]
# print(list)

# list = [1,3,5,7,2,8,4,6,9]
# check = 1
# while check != len(list)-1:
#     if list[check-1] > list[check]:
#         idx = check
#         while list[idx-1] > list[idx]:
#             list[idx-1], list[idx] = list[idx], list[idx-1]
#             # print('in')
#             # print(list)
#             # print('in')
#             idx -= 1
#     check +=1
#     # print('-------==========---------')
#     # print(list)
#     # print('-------==========---------')
# print('---------')
# print(list)
#
# def hello(age, name='yongseok', name2 = 'yumeno'):
#     print('hello', age, name,name2)
# hello(100)

# def abs(value):
#     return [v if v >0 else -v for v in value]
#
# print(abs([1,2,3,-1,-2,-3]))
# print(abs(i for i in range(-3, 3)))
# print((i for i in range(-3,3)))
# def my_gen(n):
#     for i in range(n):
#         yield i*10
#
# list = [i for i in my_gen(5)]
# print(list)
#
# gen = my_gen(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def my_gen(n):
#     for i in range(n):
#         yield i * 10
#
#
# list = [i for i in my_gen(5)]
# print(list)


# def my_range(*n):
#     start = 0
#     end = 0
#     step = 1
#
#     if len(n) == 1:
#         end = n[0]
#     elif len(n) >= 2:
#         start = n[0]
#         end = n[1]
#         if len(n) == 3:
#             step = n[2]
#
#     while start <= end:
#         yield start
#         start += step
#
# for i in my_range(0,100,3):
#     print(i)


def add(first, second):
    return first+second
def sub(first, second):
    return first-second
#
# def executor (func, op , param1, param2):
#     return func[op](param1, param2)
#
# func = {'+':add, '-':sub}
# print(executor(func, '+',5,4))
# print(executor(func, '-',5,626))

#
# def get_func(op):
#     if op == '+':
#         return add
#     else:
#         return sub
#
# result = get_func('+')(1,4)
# print(result)
#
#
# def calculate(op, num1, num2):
#     def add(first, second):
#         return first + second
#
#     def sub(first, second):
#         return first - second
#
#     if op == '+':
#         return add(num1, num2)
#     else:
#         return sub(num1,num2)
#
# print(calculate('+',5151,232))

# def func():
#     value=2
#     def nested_func():
#         # nonlocal value
#         # value = 3
#         print('nesed', value)
#     nested_func()
#     print('outer', value)
#
# func()

# def func():
#     print('hello')
# func()
#
# def func():
#     print('bye')
# func()
#
# selection = int(input())
# if selection ==1:
#     def func():
#         print('hello')
# else:
#     def func():
#         print('bye')
#
# func()

# def sacle_up():
#     scale = 2
#     def calculate(number):
#         return scale**number
#     return calculate
#
# func = sacle_up()
# print(func)
# print(func(10))

# s='abasdcdc'
# list1 = list(s)
#
# print(list1)
#
# print(list2)


