array = [4, 7, 2, 8]

n= len(array)
#Outer loop iterates to n-1, it depends on how any times the inner loop iterates
for i in range(n-1): 
    min_idx= i #Set minimum index/value to i
    for j in range(i+1, n):  #Goes through array, finds shortest value, moves it to front, one less value each loop 
        if array[j]< array[min_idx]:  #Compare to find lowest value
            min_idx = j #Store the min value in min_idx
    array[i], array[min_idx] = array[min_idx], array[i] #Swap
        
print("Sorted array:", array)

# Time Complexity: O(n^2)   - n values, n times comparison : n x n = n^2
# Space Complexity: O(1)    - No extra space needed, hence O(1)