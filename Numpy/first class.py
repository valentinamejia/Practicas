import numpy as np

a = np.array([1, 2, 3, 4])
print(type(a)) #numpy array

a.dtype # means de type for numpy library, would be int64

a[0] #access to a value in position in 0

#arrays should be the same type, int, float, etc

a.ndim #dimension
a.shape #returns a tuple number of elements in each dimension. equivalent to size in matlab
a.size #total number of elements and not the dimension

a = np.array([11, 2, 3, 4])
f = np.array([1.2, 2.3, 4.5, 6.7])

a + f #treats them elemnt by elemet with same position. element wise from all the array
f ** a # vectorize operation without the looping concept for every element

#----------- UNIVERSAL FUNCTIONS ( ufuncs)
# mathematical functions that optimize into arrays

np.sin(a) # every element of a convert for the sin(a)

a = np.array([[0, 1, 2, 3], [10, 11, 12, 13]]) #2D dimension, list of two list
a.size # 8 elements 2 row of 4 columns 2*4 = 8
a.shape # returns (2,4) 2 rows 4 columns
a.ndim # 2D
print(a[1,3]) # returns an element
print(a[1]) #returns the array

#-------------- SLICING --------
# how to get a whole column or rows in matrix
#var[ lower:upper: step]
# the lower bound element is included but the upper element is not [)

a = np.array([0, 1, 2, 3, 4])
a[1:3] #the second element till the third one, remember the fourth doenst included
a[1:-2] # form the second position till the penúltimo position
a[-4:3] #another way to say the upper thing

# omitted bounderies are assumed to be the beginning or the end of the list

a[:3] #from the 0 position till the thrid one, return 3 elements
a[-2:] # from third one till the last one
a[::2] # every element with a jump of two


a = np.arange(25).reshape(5,5) # creates an array of 25 elements and divide them by 5*5 square
print('\n', a, '\n')
print('last row:\n', a[4:])
print('from every row, from the first column till last one in jumps of 2:\n', a[:, 1::2])
print('from first row till last one in jumps of two, from beginning of column till third umps of 2:\n', a[1::2,:4:2])

a = np.array([-1, -3, 1, 4, -6, 9, 3])
mask = np.array(a < 0, dtype=bool) # if they met the condition (-) they are true, otherwise false
negative = a < 0 # indices position of negative numbers
print(a)
print(mask)
print(a[negative])
a[negative] = 0
print(a)

#------------EXCERCISE: FANCY SLICING------------------
a= np.arange(25).reshape(5,5)
# position of the elements one by one
print(a[[0, 2, 3, 3], [2, 3, 1, 4]])

# how to selesct the numbers divisible by three
mask = a%3 == 0
print(mask)
print(a[a % 3 == 0]) #only returns the numbers that are divisble by three

np.sum() #sums all the elemets of the arrar
print(np.sum(a, axis = 0)) # sums throug the axis 0 and returns the sums of the columns, if its 2d


