array = [7, 12, 5, 16, 9, 1, 4]
n= len(array)

#Outer loop iterates to n-1, it depends on how any times the inner loop iterates
for i in range(n-1):
    for j in range(n-i-1):    #Inner loop iterates the whole array while comparing to find the highest value, swaps each time it finds a highest value 
        if array[j]>array[j+1]: #Compare to find highest value
            array[j], array[j+1] = array[j+1], array[j] # Swap 
print("Sorted array:", array)

# Time Complexity: O(n^2)   - n values, n times comparison : n x n = n^2
# Space Complexity: O(1)    - No extra space needed, hence O(1)

#What if you find the sorted array in the 3rd iteration itself, there is no need of swapping further!
# Hence, this can be improved by just adding True, False statements, to break the loop and stop the algorithm


array = [7, 12, 5, 16, 9, 1, 4]
n= len(array)
for i in range(n-1):
    swapped= False # Improvement in the Bubblesort.
    for j in range(n-i-1):    
        if array[j]>array[j+1]: 
            array[j], array[j+1] = array[j+1], array[j]  
            swapped = True
    if not swapped:
        break
print("Sorted array:", array)
