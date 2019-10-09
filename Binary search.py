list = [1,3,6,9,12,15,18,21,]

head = 0
top = len(list)-1

search = 14

print('start')

while True:
    mid = (top + head) // 2
    print('head', head)
    print('top', top)
    if head > top:
        print('없다')
        break
    if list[mid] == search:
        print(mid, '번째 인덱스에 있음')
        break
    elif list[mid] > search:
        top = mid-1
    elif list[mid] < search:
        head = mid+1


print("end")

# def b_search(value, list, low, high):
#     if low > high:
#         return -1
#     mid = (low+high)//2
#     if list[mid] == value:
#         return mid
#     if list[mid] > value:
#         return b_search(value, list, low, mid-1)
#     if list[mid] < value:
#         return b_search(value, list, mid+1, high)
#
# print('result index = ', b_search(16,list,0,7))
