'''It takes one value at a time from the unsorted array and puts it ino the right place in sorted array, until the array is sorted'''
"""Take one value of unsorted array, place it in the correct oreder, repeat"""
'''The insertion sort algorithm must run through array n -1 times for array with n values'''
#Remember: First value in the array is always considered to be sorted

array = [7, 12, 5, 16, 9, 1, 4]
n= len(array)

#Outer loop iterates to n-1, it depends on how any times the inner loop iterates
for i in range(1, n):
    insert_idx = i                #Insertion index
    curr_val = array[i]           #Store value with i index
    for j in range(i-1 ,-1, -1):  #Reverse order starts with i-1 and down to 0, (does not include -1) stops at -1, last -1: Decrement by 1
        if array[j]>curr_val:     #Compare
            insert_idx = j        #Other values move up and down to adjust, so instead just shift the necessary values
            array[j+1]= array[j] 
        else:
            break
    array[insert_idx]= curr_val
print("Sorted Array:", array) 


# Time Complexity: O(n^2)   - n values, n times comparison : n x n = n^2
# Space Complexity: O(1)    - No extra space needed, hence O(1)