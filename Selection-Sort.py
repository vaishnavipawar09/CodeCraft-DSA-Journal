array = [4, 7, 2, 8]

n= len(array)
for i in range(n-1):
    min_idx= i
    for j in range(i+1, n):
        if array[j]< array[min_idx]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]
        
print("Sorted array:", array)