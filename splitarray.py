def splitArr(arr, n, k): 
    for i in range(0, k): 
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
          
        arr[n-1] = x
          
  
# main
arr = [15, 35, 12, 8, 45, 32]
n = len(arr)
position = 3
  
splitArr(arr, n, position)
  
for i in range(0, n): 
    print(arr[i], end = ' ')