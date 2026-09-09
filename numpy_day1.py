import numpy as np 

print(np.__version__)

#To create matrix
result = np.array([[1,2,3,4],[5,6,7,9],[3,4,5,6]])

print(result)
print(type(result))
print(result.shape)   #(r,c) where r = row number, c = column number

print("^"*15)

#victor
num = [12,34,5,32,11]
total = np.array(num)
print(total)
print(total.shape)

