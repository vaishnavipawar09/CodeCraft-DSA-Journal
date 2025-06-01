#Searches through an array and returns the index where it is found.

#Create a Function for Linear Search
def linearSearch(arr, targetval):
    for i in range(len(arr)):           #loop through the whole array
        if arr[i] == targetval:         #Check if currval matches the target value
            return i                    #Return the index where found
    return -1                           #Return -1, if value not found

arr = [10, 2, 5, 8, 2, 7, 9]
targetval = 9
res = linearSearch(arr, targetval)      #Call the linear function

if res != -1:
    print("Value", targetval, "found at index", res)
else:
    print("Value", targetval, "not found")
    
#Time Complexity: O(n)      Loops through whole array and compares n values
#Space Complexity: O(1)     No extra space required