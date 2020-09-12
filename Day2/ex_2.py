#파일 읽고 쓰기

# 데이터 작성 예제
# f = open('test.txt','w',encoding='utf-8')
# f.write('파이썬 기초 입니다.')
# for i in range(1,101):
#     f.write("%d번째 줄입니다\n"%i)
# f.close()



# 데이터 읽어오기-1
# readline() : 한줄씩 데이터를 읽어오는 함수

# f = open('test.txt','r',encoding='utf-8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f.close()



# 데이터 읽어오기 -2 
# readlines()

# f = open('test.txt','r',encoding='utf-8')
# # print(f.readlines())
# lines = f.readlines()
# for i in lines:
#     print(i)
# f.close()


#데이터 읽어오기 -3
# read()
# f = open('test.txt','r',encoding='utf-8')
# print(f.read())
# f.close()



# 데이터 추가하기
# add()

# f = open('test.txt','a',encoding='utf-8')
# for i in range(101,201):
#     f.write('%d번째 줄입니다.\n'%i)
# f.close()


#연습문제

f = open('numbers.txt','r',encoding='utf-8')
lines = f.readlines()
s = 0
for i in lines:
    s = s + int(i)
print(s)
f.close()



