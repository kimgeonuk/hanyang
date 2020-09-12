import pandas as pd

# a = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# b = pd.DataFrame([1,2,3,4,5],index=['a','b','c','d','e'])
# print(a)
# print(b)

# df = pd.DataFrame({
#     'a':[4,5,6],
#     'b':[7,8,9],
#     'c':[10,11,12]
# },index=[1,2,3])
# # print(df)

# # print(df[['a','b']])

# df['c'] = [2,3,4]
# df['d'] = [5,3,4]

# val = pd.Series([5,6], index=(2,3))
# df['add'] = val
# df['filter'] = df['b'] > 8

# print(df.head())
# print(df.tail(2))
# print(df.sample(1))r

# print(df)
# print(df.loc[1:2])
# print(df.loc[1:2,'a':'c']) # 행, 열 이름으로 추출
# print(df.iloc[0:2,0:3]) # numpy 인덱싱 기준

# print(df[df['a'] > 4])
# print(df[(df['a']>4) & (df['a'] < 6)])

df = pd.read_csv('서울특별시 동대문구_동대문구 코로나 행정동별 확진자 수_20200713.csv', encoding='cp949')
print(df.info())
print(df.shape)
print(df.tail())
print(df.describe())

print(df['확진자 수'].sum())






# x_1 = range(100)
# y_1 = [value for value in x_1]

# x_2 = range(100)
# y_2 = [value**2 for value in x_2]

# plt.subplot(2,1,1)
# plt.plot(x_1, y_1)
# plt.subplot(2,1,2)
# plt.plot(x_2, y_2)
# plt.show()


# x_1 = range(50)
# y_1 = [value**2 for value in x_1]
# plt.bar(x_1, y_1, width=0.5, color='r')
# plt.show()

# x_2 = range(100)
# y_2 = np.random.rand(100) * 100 # 0~1 사이에 랜덤한 값
# for i in range(0,100):
#     if i >50:
#         plt.scatter(x_2[i], y_2[i], color='r', s=y_2[i])
#     else:
#         plt.scatter(x_2[i], y_2[i], color='b', s=y_2[i])
# plt.show()

labels = ['apple','banana','orange','cherry']
size = [10,20,30,40]
explode = (0,0.1,0,0)
plt.pie(size, explode=explode, labels=labels, startangle=90)
plt.show()