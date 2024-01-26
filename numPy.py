import numpy as np

# 1. Array 1D
# array_1d = np.array([1,2,3]) # => [1 2 3]
# Dimention
# array_1d_d = array_1d.ndim # => 1

# List to array
# mylist = [1,2,3,4]
# l_to_arr = np.array(mylist) # => [1 2 3 4]

#####################################################

# 2. Array 2D
# array_2d = np.array([[1,2,3], [4,5,6]]) 
'''
[[1 2 3]
 [4 5 6]]
'''
# เข้าถึงข้อมูลใน Array
# print(array_2d[1][2]) # => 6

#####################################################

# 3. Array 3D
# array_3d = np.array([[[1, 2, 3], [4, 5, 6]],[[10, 11, 12], [13, 14, 15]]])
# arr_3d_d = array_3d.ndim # => 3
# print(array_3d[0][1][2]) # => 6
# print(array_3d)
'''
[[[ 1  2  3]
  [ 4  5  6]]

 [[10 11 12]
  [13 14 15]]]
'''

#####################################################

# 4. Data type (dtype)
'''
int, float, string, boolean, complex, object
'''

# arr_a = np.array([1,2,3,4,5])

# check datatype
# print(arr_a.dtype) # => int32 //(32bit)

# declear dtype
# arr_b = np.array([7,8,9], 'float')
# print(arr_b.dtype) # => float64

# arr_c = np.array(['1', '2', '3'], 'int32')
# print(arr_c.dtype) # => int32

#####################################################

# 5. Matrix (array 2 มิติ) 

# Zero matrix
# arr_zero = np.zeros((3,3), 'int32')
# print(arr_zero)
'''
[[0 0 0]
 [0 0 0]
 [0 0 0]]
'''

# Ones matrix
# arr_ones = np.ones((5,5), 'int32')
# print(arr_ones)
'''
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
'''

# Indentity matrix
# arr_identity = np.identity(4, 'int32')
# print(arr_identity)
'''
[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]]
'''

# matrix constant
# arr_const = np.full((3,3), 10, 'int32')
# print(arr_const)
'''
[[10 10 10]
 [10 10 10]
 [10 10 10]]
'''

# Empty array เป็นการสร้าง array ตามขนาดที่เราต้องการโดยไม่ได้สนใจข้อมูล
# arr_empty = np.empty((3,4), 'int32')
# print(arr_empty)
'''
[[-2147483647          20           0           0]
 [          0        1281    83886080          21]
 [  921830550  1341958235  -796617073        1001]]
'''

# Linspace create array 1D (start, stop, size) ระบุจำนวน
# arr_linsp = np.linspace(1,5,10)
# print(arr_linsp)
'''
[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
 3.66666667 4.11111111 4.55555556 5.        ]
'''

# Arange (start, stop, step) ระบุ step
# arr_arange = np.arange(1,10,2)
# print(arr_arange)
'''
[1 3 5 7 9]
'''

# Random 
# .random 
# arr_rand = np.random.random((2,2))
# print(arr_rand)
'''
[[0.77403853 0.49335133]
 [0.40005113 0.58687192]]
'''

# arr_rand = np.random.rand(5)
# print(arr_rand)
'''
[0.0888873  0.62911801 0.84966275 0.5200881  0.97617579]
'''

#####################################################

# 6. Reshape & Resize
# arr_a = np.arange(10)
# print(arr_a)
'''
[0 1 2 3 4 5 6 7 8 9]
'''
# Reshape
# arr_b = arr_a.reshape((2,5))
# print(arr_b)
'''
[[0 1 2 3 4]
 [5 6 7 8 9]]
'''

#####################################################

# 7. Flatten to array 1D
# arr_a = np.array([[1,2], [3,4], [5,6]])
# arr_flatt = arr_a.flatten()
# print(arr_flatt) # => [1 2 3 4 5 6]

#####################################################

# 8. Function in numpy 
# arr_a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr_a.sum()) # => 45
# print(arr_a.prod()) # => 362880
# print(arr_a.mean()) # => 5.0
# print(arr_a.max()) # => 9
# print(arr_a.min()) # => 1

# arr_b = np.array([[10,20,30], [40,50,90], [80,100,5]])
# print(np.min(arr_b,0)) #=> [10 20  5]

#####################################################

# 9. dot product
# arr_a = np.array([[1,2], [3,4]])
# arr_b = np.array([[11,12], [13,14]])
# dot_ab = arr_a.dot(arr_b)
# print(dot_ab)