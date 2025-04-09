'''It is divide and conquer algorithm that sorts an array by first breaking it into sub arrays and then my merging them together'''
'''Two functions are needed, one for sorting and one to merge them back together'''

def merge(arr, L, M, R):
    left, right= arr[L:M+1], arr[M+1:R+1] # does not include the last value hence used + 1
    i, j, k = L, 0, 0  # i for arr, j for left, k for right

    while j < len(left) and k < len(right):
        if left[j] <= right[k]:
            arr[i] = left[j]
            j += 1
        else:
            arr[i] = right[k]
            k += 1
        i += 1      # Irrespective of j and k , i should get incremented

    while j < len(left):
        arr[i] = left[j]
        j += 1
        i += 1

    while k < len(right):
        arr[i] = right[k]
        k += 1
        i += 1

def mergesort(arr, l, r):
    if l == r:
        return arr

    m = (l + r) // 2            #Calculate mid value
    mergesort(arr, l, m)        #Left sub array
    mergesort(arr, m + 1, r)    #Right sub array
    merge(arr, l, m, r)
    return arr

# Example usage
nums = [12, 7, 1, 6, 18, 9]
sortedArr = mergesort(nums, 0, len(nums) - 1)
print("Sorted array:", sortedArr)

#Time Complexity: O(n log n)
#Space Complexity: O(n)  - As it uses recursion
