def rotateArray(a,d):
    temp = []
    n=len(a)
    for i in range(d,n):
        temp.append(a[i])
    i = 0
    for i in range (0,d):
        temp.append(a[i])
    a=temp.copy()
    return a
 
arr = [7, 6, 5, 4, 3, 2, 1]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 3))
