import numpy as np

# list_a = [1,2,3]
# list_b = [4,5,6]

# lsum = list_a + list_b
# print(lsum)

# np_list_a = np.array([1,2,3])
# np_list_b = np.array([4,5,6])

# nsum = np_list_a + np_list_b
# print(nsum)


# ndArray_A = np.array([1,2,3])
# ndArray_B = np.array([[1,1,1],[2,2,2]],dtype=float)

# print(ndArray_A)
# print(ndArray_B)

# print(ndArray_A.shape)
# print(ndArray_B.shape)

# zeros = np.zeros([4,2], dtype=float)
# print(zeros)

# ones = np.ones([4,2],dtype=float)
# print(ones)

# eye = np.eye(3)
# print(eye)

# eye = np.eye(4,k=1)
# print(eye)

# arr = np.array(range(1,9))
# print(arr)

# arr2 = arr.reshape(-1,2)

# print(arr2)

# print(arr2.flatten())

# a = np.array([[1,2,3],[4.5,5,6]], dtype=int)
# a[1,0] = 5
# print(a)

list_A = [[1,2,5,8],
            [1,2,5,8],
            [1,2,5,8],
            [1,2,5,8]]

a = np.array(list_A, dtype=int)
# print(a)

# print(a[0:2,1:3])
# print(a[1,:])

# indexing = a > 3
# print(indexing)

# a[indexing] = 0
# print(a)

a = np.arange(1,13)

a = a.reshape(3,4)
print(a)

print(a.sum(axis=0))
print(a.sum(axis=1))