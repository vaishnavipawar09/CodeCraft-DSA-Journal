'''One of the fastest sorting algorithms - It takes array, chooses pivot, lower values to left, higher to right, uses recursion'''
'''Swap pivot with higher values so that pivot element lands in between the lower and higher values, repeat for sub arrays on left and right'''
'''It makes the sub array shorter and shoreter until the array is sorted'''

def partition(array, low, high):
    pivot = array[high]                               #set pivot to the last value
    i = low - 1                                       #Set i to -1, start of the array
    for j in range(low, high):
        if array[j] <= pivot:                         #Compare with pivot
            i += 1                                    #Increment of i by 1
            array[i], array[j] = array[j], array[i]   #Swap i and j valuees eg [12, 7, 11] 11 is pivot. here 7 is on left so first swap 7 & 12, i and j]
            
    array[i+1], array[high] = array[high], array[i+1] #Swap i+1 and high valuees eg [7, 12, 11] 11 is pivot(high). here 12 is on right so swap 11 & 12 now which is i+1 and high
    return i + 1 

        
def quicksort(array, low = 0, high = None):
    if high is None:
        high= len(array) - 1
        
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)  #Runs through the left side of pivot
        quicksort(array, pivot + 1, high) #Runs through the right side of pivot
    
array = [7, 12, 5, 16, 9, 1, 4]
quicksort(array)
print("Sorted array:", array)

# Time Complexity: 
#               Worst Case:  O(n^2)   - n values, n times comparison : n x n = n^2
#               Average Case: O(n log n)
# Hence as the avg case is faster, quick sort is faster than Bubble Sort, Selection Sort and Insetion Sort

# Space Complexity: O(1)    - No extra space needed, hence O(1)