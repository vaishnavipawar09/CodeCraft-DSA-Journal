'''Sorts an array by individual digits, staring with the ;least significant digit(the one at the units place)'''
'''It is a non comparative algorithm that only works on non negative integers'''


array = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", array)
radixarray = [[], [], [], [], [], [], [], [], [], []]  #Created a radix array wih buckets to store, total 10(0 to 9)
maxval = max(array)
exp = 1

while maxval // exp > 0:
    while len(array)> 0:
        val = array.pop()                       #Remove from the array
        radixindex = (val // exp ) % 10
        radixarray[radixindex].append(val)      #Store in the radix array
        
    for bucket in radixarray:                   #From bucket back to the main array
        while len(bucket)> 0:
            val = bucket.pop()                  #Remove fom the bucket 
            array.append(val)                   #Back to its place
            
    exp +=10
    
print("Sorted Array:", array)                   #Sorted Array


#Time Complexity = (n. log n )
#dix sort has a space complexity of O(n + b), where n is the number of elements and b is the base of the number system used.
