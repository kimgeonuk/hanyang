# 자료형 [리스트]

# a = []
# a = list()
# print(a)

# a = [1,2,3,4,5,6,7]
# b = [1,2,['a','b']]
# print(b[-1][0])
# print(b)
# print(a[0:5]) #리스트 범위 출력
# a[2] = 5 # 리스트 수정
# print(a)

# del a[2] #리스트 삭제
# print(a)



# a = [1,2,3,4,5,6,7]

# a.append([1,2]) #리스트 값 추가
# print(a)

# a.insert(1,10) #리스트 특정한 위치에 값 추가
# print(a)

# print(a.index(3))
# print(a.index(100))


# a = [1,5,2,3,5,6,7,2]

# a.sort() # 오름차순 정렬
# a.reverse() # 역순 정렬
# a.sort(reverse=True) #내림 차순 정렬
# print(a)

# c = a.pop(0)
# # print(c)
# print(a)


#튜플
# a = (1,2)
# a[0] = 5


# 딕셔너리

# a = {}
# a = dict()
# a = {1 : 'one', 2: 'two', 3 : 'three'}
# f = {'a' : 'apple', 'b' : 'banana', 'c': 'chery'}
# print(f['a'])

#삭제
# del a[1]
# print(a)

# print('e' in f) # 딕셔너리 에 키 값이 존재하는지 확인

# print(f.keys()) #키에 값을 확인할때
# print(f.values()) #딕셔너리에 값을 확인할 때

# a = {1 : 'one', 2: 'two', 3 : 'three'}
# f = {'a' : 'apple', 'b' : 'banana', 'c': 'cherry'}

# f['o'] = 'orange'
# # print(f)
# # f['a'] = 'app'
# print(f)

# f.clear()
# print(f)

# Bool 자료형 True False

# print(1 == 1)
# print(2 > 1)
# print(2 < 1)
# print('a' == 'a')
# print([1,2] == [1,2])

# a = 'a'
# print(bool(a))

# a = '881225-1524785'

# print(a[0:6])
# c = a.split('-')
# print(c[0])

# print(a[7])