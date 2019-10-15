#=================================================================
# Hello World
#=================================================================
# print("Hello")
# message = "Hello"
# print(message)

#=================================================================
# 변수 사용해 보기
#=================================================================
# name = 'yong'
# age  = 25
# age  = 23
# score = 4.3

# print(name)
# print("hello" + name)
# print("hello", name) # ,는 띄어쓰기 하고 붙임
# print(name, age)
# print(age, score)

#=================================================================
#input
#=================================================================
# str_test = input("String : ")
# int_test = int(input("Int : "))
# float_test = float(input("Float : "))

# print(str_test, int_test, float_test)

#=================================================================
#variable_test
#=================================================================
# num1 = 10
# num2 = 20
# print("num1 + num2 =",num1+ num2)

#=================================================================
#variable_test2
#=================================================================
# num_int = 35
# num_float = 20.88
# print(num_int + num_float) # 자동으로 형변환해서 float가 된다

# my_input = input("input String : ")
# print("입력 내용 : " + my_input)

#=================================================================
#variable_test3
#=================================================================
# get_name = input("your name? : ")
# print("Hello,", get_name)

#=================================================================
#variable_test4
#=================================================================
# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)


#=================================================================
#list
#=================================================================
# list = []
# list2 = [1,2,3, True, False]
# list3 = [(1,2,3), {"name" : "user"}, [1,2,3]]
# list4 = [list, list2]
# print(list,list2)
# print(list3)
# print(len(list4), list4)


#=================================================================
#lsit_test
#=================================================================
# list = [1,2,3,4,5]
# print(list[2])


#=================================================================
#list_test2
#=================================================================
# list = [0,1,2,3,4,5]
# print(list.index(2))
# list.insert(3, -1)
# print(list)
# list.append(6)
# print(list)
# list.extend([7,9,8])
# print(list)
# list.sort()
# print(list)
# list.reverse()
# print(list)

#=================================================================
#list_test3
#=================================================================
# list = [1,2,3,4,5]
# list.insert(0,6)
# list.append(0)
# print(list)
# list.sort()
# print(list)

#=================================================================
#list_test4
#=================================================================
# list = [1,2,3,4,5]
# del list[1]
# print(list)
# list.remove(1)
# print(list)
# del list[list.index(3)]
# print(list)

#=================================================================
#list_test5
#=================================================================
# list = [1,2,3,4,5]
# user_num = int(input())
# list.remove(user_num)
# print(list)

#=================================================================
#list_test6
#=================================================================
# list = [0,1,2,3,4,5,6,7,8]

# print(list[0], list[1])
# print(list[-1], list[-2])

#=================================================================
#list_test6
#=================================================================
# rect = (10, 10, 100, 100)
# rect2 = 20, 20, 50, 50
# print(type(rect), type(rect2))
# print(rect[1])
# print(rect2)

#=================================================================
#string
#=================================================================
# first = "Hello 'friend'"
# second = 'Hello "friend"'
# third = """
# Hello
# friend
# """

# fourth = '''
# Hello!
# friend!
# '''
# print(first, second)
# print(third)
# print(fourth)

#=================================================================
#string and list
#=================================================================
# str = 'Hello everyone'
# arr = str.split()
# print(arr)
# arr2 = list(str)
# print(arr2)
# str2 = ':'.join(arr2)
# print(str2)
# str3=''.join(arr2)
# print(str3)

#=================================================================
#Slicing
#=================================================================
# list = [0,1,2,3,4,5,6,7,8,9]
# print(list[5:8])
# print(list[7:])
# print(list[:4])
# print(list[2:5:2]) # start : 2 end : 5 그리고 2칸씩 간격으로 출력

#=================================================================
#Slicing2
#=================================================================
# list = [0,1,2,3,4,5,6,7,8,9]
# print(list[-1])
# print(list[-3])
# print(list[:-3])
# print(list[-5:])

# list2 = list[::-1]
# print(list2)

#=================================================================
#Slicing3
#=================================================================
# user_string = input()
# print(user_string[:3])
# print(user_string[-3:])

#=================================================================
#dictionary
#=================================================================
# capitals = {'Korea':'Seoul', 'UK': 'London'}
# days = {1:31, 2:28, 3:31, 4:40}
# print(capitals['Korea'])
# print(days[3])
# days[5] = 31 # 항목 하나 추가
# print(days)
# del capitals['UK'] # 'UK' 키를 이용한 삭제
# print(capitals)
# capitals.update({'USA':'Washington, D.C.', 'China':'Beijin'}) #update 라기 보다는 extend 여러개 추가에 가깝네
# print(capitals)

#=================================================================
#Set
#=================================================================
# set1 = set([1,2,3,1.1,2.1,3.1, 'Hello'])
# set2 = {(1,2),3,4, 'Hello'}
# print(set1); print(set2)
# print(set1 & set2)
# print(set1.intersection(set2))
# print(set1 | set2)
# print(set1.union(set2))
# print(set1-set2)
# print(set1.difference(set2))
# set1.remove('Hello')
# set1.add(4)
# set1.update([5,6])
# print(set1)

#=================================================================
#Set
#=================================================================

# a=20
# b=30
# c=6
# d=4

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/d)
# print(a%c)
# print(c**d)
# print(a//c)

# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)

# a=True
# b=False
# c=True

# print(a and b)
# print(a and c)
# print(a or b)
# print(not a)

#=================================================================
#if
#=================================================================
# var = int(input())
# if var > -1:
#     print("OK")
# else:
#     print("NG")

#if2

# user_passwd = input("your password : ")

# if(len(user_passwd) >= 8):
#     print("OK")
# else:
#     print("NG")

#if3

# num1 = int(input())
# num2 = int(input())
# if num1>=0 and num2 >=0:
#     print("OK")
# elif(num1<0 and num2<0):
#     print("NG")
# else:
#     print("soso")

#if4

# num1 = int(input())

# if num1%2 == 0:
#     print("even")
# else:
#     print("odd")

#if5

# age =18 
# if age > 19:
#     print('adult')
# elif 19>=age>12:
#     print('teenager')
# else:
#     print('kid')

#if6

# num = input()

# if 10>= len(num) >=4:
#     print('OK')
# else:
#     print('NG')

#if7

# age = 18
# print("Hello") if age > 19 else print('Too young')
# print('Hello' if age > 19 else 'Too young')

#if8
# n1 = int(input())
# n2 = int(input())

# print('OK' if n1+n2>-1 else 'NG')

#if9

# n1 = int(input())
# n2 = int(input())
# mm = input()

# print(n1+n2 if mm=='+' else n1-n2)

#for1

# arr = [1,2,3,4,5]
# for i in arr:
#     print(i, end=' ')
# for i in [2,4,6,8]:
#     print(i, end=' ')
# for i in arr[2:]:
#     print(i, end=' ' )

#for2
# tp = (1,2,3,4,5)
# for i in tp:
#     print(i)
# str = 'Hello everyone'
# for s in str:
#     print(s)

# #for3
# list = [1,2,3,4,5,6,7,8,9]

# for i in int(list):
#     print(i[::2])

#for4
# list = [1,2,3,4,5,6,7,8,9]
# sumE = 0
# sumO = 0
# for i in list:
#     if i % 2 == 0:
#         sumE += i
#     else:
#         sumO +=i
# print(sumE)
# print(sumO)

#for
# for i in range(1, 10):
#     print(2, 'x', i, '=', 2*i)

#for astarisk
# for i in range(5):
#     for j in range(i+1):
#         print('*', end='')
#     print()

#for enumerate : 반목문 중 index를 알고 싶을 때 사용!
# for index, value in enumerate([0,2,4,6,8,10]):
#     print(index, value)
# for i, va in enumerate(['john', 'Kate', 'Sam', 'Mary']):
#     print(i, va)

#for zip
# arr1 = [1,2,3,4,5]
# arr2 = [9,8,7,6,5]
# arr3 = [10,20,30,40,50]
#
# for i, j in zip(arr1,arr2):
#     print(i, j)
# for i, j, k in zip(arr1, arr2, arr3):
#     print(i,j,k)

#for list comprehension
# arr = [ i for i in range(5,10)]
# print(arr)
# arr2 = [i*2  for i in range(3)]
# print(arr2)
# arr3 = [i*j for i in range(1,4)
#             for j in range(1,4)]
# print(arr3)

# arr = [i for i in range(1, 11, 2)]
# print(arr)
# arr2 = [i*3 for i in range(1,11)]
# print(arr2)
# #Woww

#if+for
# arr = [i for i in range(10) if i%2 == 0]
# print(arr)
# scores = [80,95,66,80,88,70,74,98]
# a_grade = [s for s in scores if s > 90]
# print(a_grade)

#test1 쉬는시간에 다시해보자
# arr = [i for i in range(5)]
# arr=[]
# for i in range(5):
#     arr.append(int(input('come on')))
# arr2 = [i for i in arr if i > 0 ]
# print(arr)
# print(arr2)

#comprehension
# arr_id=['학생1', '학생2', '학생3', '학생4', '학생5']
# arr_score = [90,80,70,80,99]
# dic = {key : value for key , value in zip (arr_id, arr_score)}
# print(dic)

#set
# set1 = {i for i in range(5)}
# print(set1)
# arr = [1,1,2,3,4,3,3,]
# set2 = {i for i in arr}
# print(set2)

#while test
# sum = 0
# user = int(input('input'))
#
# while True:
#     user = int(input('input'))
#     if user == 0:
#         break
#     else:
#         sum += user

#test2
#
# value_sum = 0
# value= int(input())
# count =0
# while value != 0:
#     value_sum += value
#     count  += 1
#     value = int(input())
# print(value_sum/count)
#
# varr=[]
# value=int(input())
# while value != 0:
#     varr.append(value)
#     value = int(input())
# print(sum(varr)/len(varr))

# list = [1,7,3,8,5,9]
# flag=0
# for i in range(len(list)):
#     flag = i
#     for j in range(i,len(list)):
#         if list[flag] > list[j]:
#             flag = j
#     list[flag], list[i] = list[i],list[flag]
#
# print(list)

# list = [55,1,78,12,42]
# for i in range(len(list)):
#     for j in range(len(list)-i-1):
#         print(j)
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
#         print(list)

# list = [1,3,5,7,2,8,4,6,9]
#
# for i in range(len(list)):
#     for j in range(i,0,-1):
#         print(j)
#         if list[j-1] > list[j]:
#             list[j-1], list[j] = list[j], list[j-1]
#             # print(list)
#
#     print('==========')
