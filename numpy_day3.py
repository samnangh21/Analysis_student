import numpy as np #import Numpy library

a = np.arange(0, 10, 2) #it starts from 0 and increase by 2 until 8

print(a)

b = np.arange(100, 10, -2) #it starts to decrease by -2 from 100 to 10
print(b)

print("*"*40)

c = np.linspace(5,25,3) #the line space from 5 to 25 are devided by 3 to get 3 equal space numbers
print(c)

d = np.linspace(-5,25,6)
print(d)

print("*"*40 + "1D Mathematic Operation")

#vector
n1 = np.array([2,5,7,8,1])
n2 = np.array([1,3,9,2,7])

print(n1 + n2)
print(n1 - n2)
print(n1 / n2)
print(n1 * n2)

print("*"*40 + "2D Mathematic Operation")

n3 = np.array([
    [2,5,7,8,1],
    [3,1,5,2,7]
    ])

n4 = np.array([
    [1,3,9,3,2],
    [2,6,8,3,1]
    ])

print(n3 + n4)
print(n3 - n4)
print(n3 * n4)
print(n3 / n4)

print("*"*40 + "eye")

id = np.eye(6) #it shows matrix 6x6 which has 1 as diagonal
print(id)

id2 = np.identity(4)
print(id2)

print("*"*40 + "radom arrays")

rad = np.random.randint(0,20,size=15) #it randoms range number from 0 to 20 and it select 15 elements numbers
print(rad)

rad1 = np.random.rand(6)
print(rad1)







