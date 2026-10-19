# merge sort
# ascending order
nums = [3,1,4,5,2,6, 45,20, 100,8,33,55,22,11,9,7,44,99,212,15]
print("Original array :",nums)
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left_half= arr[ :mid]
    right_half = arr[mid: ]
    left_sorted = merge_sort(left_half)
    right_sorted =  merge_sort(right_half)
    return merge_array(left_sorted,right_sorted)

def merge_array(left,right):
    merge= []
    i ,j =0,0
    
    while i <len(left) and j<len(right):
        if left[i]<=right[j]:
            merge.append(left[i])
            i +=1
        else:
            merge.append(right[j]) 
            j +=1  
    while i < len(left):
         merge.append(left[i])
         i +=1
    while j <len(right):
        merge.append(right[j])
        j +=1     
    return merge   
merge_array = merge_sort(nums)
print("Ascending order : ", merge_array)

# Decending order

nums = [3,1,2,4,1,5,2,6,4]
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left_half= arr[ :mid]
    right_half = arr[mid: ]
    left_sorted = merge_sort(left_half)
    right_sorted =  merge_sort(right_half)
    return merge_array(left_sorted,right_sorted)

def merge_array(left,right):
    merge= []
    i ,j =0,0
    
    while i <len(left) and j<len(right):
        if left[i]>=right[j]:
            merge.append(left[i])
            i +=1
        else:
            merge.append(right[j]) 
            j +=1  
    while i < len(left):
         merge.append(left[i])
         i +=1
    while j <len(right):
        merge.append(right[j])
        j +=1     
    return merge   
merge_array = merge_sort(nums)
print("Descending order : ", merge_array)


# tc = o(n log n) in the wrost case
# sc = o(n) due to the temporary arrays used for merging
