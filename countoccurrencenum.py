def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
 
lst = [45, 96, 45, 96, 45, 45, 96, 25, 45]
x = 45
print('{} has occurred {} times'.format(x,
                                        countX(lst, x)))
