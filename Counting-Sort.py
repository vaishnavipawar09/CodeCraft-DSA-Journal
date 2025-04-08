def coutingsort(array):
    maxval=max(array)                   #Calculate Max i.e. k
    count = [0] * (maxval +1)           #If highest value is n, elements must be n + 1 hence maxval + 1, Creating the Count array
    
    while len(array)>0:
        num= array.pop(0)               #Remove element from the array
        count[num] += 1                 #Increase the count of counting array
        
    for i in range(len(count)):         #Loop through the counting array
        while count[i]>0:
            array.append(i)             #Add value from the counting array to the actual array
            count[i] -=1                #Decrement the count of counting array
            
    return array        
    
    
unsortedarray = [7, 12, 5, 16, 9, 1, 4]
sortedarray = coutingsort(unsortedarray)
print("Sorted array:", sortedarray)

#Time Complexity : range of k values, number of values are n, so Time complexity is : O(n + k)
'''If k is small than n, best case TC= O(n)
   If k is big than n, worst case TC= O(n^2) '''
   
#Space Complexity : space for count array(k) and output array(n), so Space complexity is : O(n + k)