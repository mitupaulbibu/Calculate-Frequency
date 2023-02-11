def calculateFrequency(arr, n):
     
    x = {}
 
    for i in range(n):
 
        if arr[i] not in x:
            x[arr[i]] = 0
        x[arr[i]] += 1
         
    for i in x:
        print(i,  x[i])
     
arr = [1, 2, 1, 3, 1, 4, 2, 4]
n = len(arr)
 
calculateFrequency(arr, n)

