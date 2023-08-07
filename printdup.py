def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
 

list1 = [15, 15, 30, 52, 52, 30, 40,
         50, -20, 60, 50, 96, -96]
print (Repeat(list1))