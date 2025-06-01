#Searches through an array and returns the index where it is found.
#Faster than the linear search, but it needs to be sorted array for it to work
#Works by checking the center value of the array, if value small move to the center of the left subarray, 
#else move to the center of right subarray

#Create a Function for Linear Search
def binarySearch(arr, targetval):
    l, r = 0, len(arr) - 1              #Create two pointers, at start and end of the array
    
    while(l <= r):
        mid = (l + r) // 2              #Calculate the mid value
        
        if arr[mid] == targetval:       #Target found return index
            return mid
        
        if arr[mid] < targetval:         
            l = mid + 1                 #currentvalue less than target value, move to the left subarray
        else:
            r = mid - 1                 #currentvalue greater than target value, move to the right subarray
    return -1                           #Value not found return -1

arr = [10, 2, 5, 8, 2, 7, 9]
targetval = 2
res = binarySearch(arr, targetval)      #Call the Binary function

if res != -1:
    print("Value", targetval, "found at index", res)
else:
    print("Value", targetval, "not found")
    
#Time Complexity: O(log n)  Search area is always half of the previous search area, 
                        #   needs only log n comparison to look through sorted array of n values
                        
#Space Complexity: O(1)     No extra space required

#Iterative SC: O(1), Recursive SC: O(log n)