'''The classic Bucket Sort algorithm assumes that the input values are in the range [0, 1)'''
'''Divie thto buckets, use sorting algorithm on the values in the bucket, ater sorting merge them together'''

def insertionsort(bucket):             #Sorting algorithm
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i-1
        while j>=0 and bucket[j]> key:
            bucket[j+1] = bucket[j]
            j-=1
            bucket[j+1] = key
            
def bucketsort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]  #Creating buckets
    
    for num in arr:             
        bi= int(n*num)
        buckets[bi].append(num)
        
    for bucket in buckets:
        insertionsort(bucket)   
        
    index= 0
    for bucket in buckets:
        for num in bucket:
            arr[index]= num
            index +=1
    
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucketsort(arr)
print("Sorted array is:")
print(" ".join(map(str, arr)))


#Time Complexity: O(n^2)
#Space Complexity: O(n +k)