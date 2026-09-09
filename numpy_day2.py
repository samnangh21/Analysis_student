import numpy as np

# 1D vector
vector = np.array([1,2,3,4,5])

print(vector)
print(type(vector))
print(vector.shape) #count only row
print(vector.size)   # count all elements



# 2D martix
print("*"*20 + "Matrix 2D" + "*"*20)

martrix = np.array([
    [2,5,6],
    [7,5,3]
])

print(martrix)
print(martrix.size) #count all element in martrix

#---------------------------------------------
print("*"*20)

list = [22,45,11,23,65]
vector2 = np.array(list)

print(vector2)
print(vector2[3])
print(vector2[len(vector2)-1]) #it display the last number of list
print(f"output slicing: {vector2[1:4]}")


martrix_2 = np.array([
    [2,9,6],
    [7,5,3],
    [4,2,8]
])

print(martrix_2)
print(martrix_2.shape)

print(martrix_2[0,1])  #it displays the number(9) that is in row 1 and column 2
print(martrix_2[1,1])
print(martrix_2[0,:])  #it shows all elements of the first row [2 9 6]
print(martrix_2[2])    #it shows all elements of the third row [4 2 8]

#special array
print("*"*20 + "special array" + "*"*20)

zero = np.zeros(3)
print(zero)

zero_1 = np.zeros((3,6))
print(zero_1)

one = np.ones((3,3))
print(one)

# 1D
f = np.full(5,7) #it is 1D, showing 5 times of 7 in row
print(f)

#2D
f1 = np.full((2,3),7)  #it is 2D, showing element of 7 which 2 rows and 3 column
print(f1)


