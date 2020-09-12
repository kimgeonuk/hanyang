# 제어문

# if 조건문

# money = True

# if money:
#     print('택시를 타고 갑니다')
# else:
#     print('걸어서 가세요')


# money = 3000

# if money > 3000:
#     print('택시를 타고 가세요')
# elif money <= 3000:
#     print('버스를타고 가세요')
# else:
#     print('걸어가세요')


#while 반복문


# treeHit = 0

# while treeHit < 10:
#     treeHit = treeHit + 1
#     if treeHit % 2 == 1:
#         continue
#     print(f"나무가 {treeHit}번 찍혔습니다.")

#for문

#구조


# for 변수 in 범위(반복가능한변수) :
    #수행할 문장

#범위를 지정
# for i in range(0,50):
#     print(i)


#반복 가능한 변수 (리스트, 튜플, 문자열)
# f = ['apple', 'banana', 'cherry']
# for i in f:
#     print(i)

# scores = [90, 60, 65, 70, 50]
# number = 0

# for i in scores:
#     number = number+1
#     if i > 60:
#         print("%d번쨰 학생은 합격 입니다."%number)
#     else:
#         print("%d번째 학생은 불합격 입니다."%number)


# count = 0 
# result = 0

# while count < 1000:
#     count = count + 1
#     #수행문 작성
#     if count % 3 == 0:
#         result = result + count

# print(result)


# #구구단
# for i in range(1,10):
#     for j in range(1,10):
#         # print("%d x %d = %d " %(i,j,i*j)) 
#         print(f"{i} x {j} = {i*j}") #python 3.6버전 이상일떄만


f = ['사과', '딸기', '포도', '수박', '바나나', '사과', '딸기','딸기','포도']
d = {}
#d = {'사과': 1, '딸기':1, '포도':1, ''..}
for i in f:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)