#matplotlib
import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4,5],[1,3,5,7,9]) # x, y 
# plt.plot([1,2,3,4,5],[10,20,30,40,80])
# plt.ylabel('some number')
# plt.show()

# x_1 = range(100)
# y_1 = [value for value in x_1]

# x_2 = range(100)
# y_2 = [value **2 for value in x_2]

# plt.subplot(2,1,1)
# plt.plot(x_1,y_1)
# plt.subplot(2,1,2)
# plt.plot(x_2,y_2)
# plt.show()

# x_1 = range(50)
# y_1 = [value for value in x_1]

# plt.bar(x_1, y_1, width=0.2, color='r', align='edge')
# plt.show()

# x_2 = range(100)
# y_2 = np.random.rand(100) * 100 # 0~1 

# for i in range(0,100):
#     if i > 50:
#         plt.scatter(x_2[i],y_2[i], color='r', s= y_2[i])
#     else:
#         plt.scatter(x_2[i],y_2[i], color='b', s= y_2[i])

# plt.show()

labels = ['apple','banana','orange','chreey']
size = [10,20,30,40]
explode = (0,0.1,0,0)

plt.pie(size, explode=explode, labels=labels, startangle=90)
plt.show()