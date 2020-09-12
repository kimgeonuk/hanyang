# 함수

# def add(a,b):
#     return a+b

# print(add(2,3))


# def say():
#     print('안녕하세요')
#     return 'Hi'
# print(say())



# def add(*args):
#     r = 0
#     for i in args:
#         r = r + i
#     return r

# print(add(2,3,5,7,10,25,22))



# def calculator(cal, cal2, *args):
#     if cal == 'add':
#         r = 0
#         for i in args:
#             r = r + i
#     elif cal == 'mul':
#         r = 1
#         for i in args:
#             r = r * i

#     return r

# print(calculator('mul', 'add',1,2,3,4,5))


# def avg(*args):
#     r = 0
#     for i in args:
#         r = r + i
#     return r / len(args)

# print(avg(1,2,3,4,5,6,7,8,9,10))


# def add_mul(a,b):
#     return a+b, a*b

# print(add_mul(2,3)[1])

# a = input('a의 값을 입력해주세요')

# print(a)



# 1,2,3,4,5

a = input('더하고자 하는 값을 입력해주세요(구분은,)')
a = a.split(',')
s = 0
for i in a:
    s = s + int(i)

print(s)


