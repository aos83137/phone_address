stack = [None for i in range(10)]

size = len(stack)
top = -1

def push(value):
    global top
    if top < size-1:
        top += 1
        stack[top] = value
        return top
    else:
        return None

def pop():
    global top
    if top > -1:
        value = stack[top]
        del stack[top]
        top -= 1
        return value
    else:        return None

while True:
    print('---------------------------------')
    print('1:push\n2:pop\n3:print\n0:finsh')
    s = input()
    if s == '1':
        print('number', end=' ')
        num = int(input('push값 입력 '))
        print('pushed' if push(num) != None else 'stack overflow')
    elif s == '2':
        num = pop()
        print('pop: ' + str(num) if num != None else 'stack overflow')
    elif s == '3':
        list = [i for i in stack]
        print(list)
    elif s == '0':
        break



