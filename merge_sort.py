# merge two sorted array

left = [1,2,3,4]
right = [1,1,3,4,5,6,7]
def merge_array(left,right):
    result = []
    i ,j =0,0
    n,m = len(left),len(right)
    while i <n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j]) 
            j +=1   
    return(left,right)
print(merge_array(left,right))





