queuelist = []


def put(n):
    queuelist.append(n)
    ppp()

def get():
    value = queuelist.pop(0)
    ppp()
    return value

def ppp():
    print('현재 Queue', queuelist)


while True:
    print('-------------------------------------------')
    print('1:put\n2:get\n0:end')
    menu = input('메뉴 선택 : ')
    if menu == '1':
        num = int(input('삽입값: '))
        put(num)
    elif menu == '2':
        get()
    elif menu == '3':
        break

print(queuelist)
