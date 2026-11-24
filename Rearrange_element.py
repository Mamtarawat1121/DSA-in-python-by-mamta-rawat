# brute solution

def Rearrange_element():
    
 nums = [5,10,-3,-1,-10,6]
 pos = [5,10,6]
 neg = [-3,-1,-10]
 for i in range(0,len(pos)):
    nums[2*i] = pos[i]
    nums[(2*i)+1] = neg[i]
 return nums   
print(Rearrange_element())
# tc = o(n+n/2)
# sc = o(n)


# optimal solution


def Rearrange_element():
    nums = [5,10,-3,-1,-10,6]
    n = len(nums)
    result = [0]*n
    pos_index,neg_index = 0,1
    for i in range(0,n):
        if nums[i]>=0:
            result[pos_index] = nums[i]
            pos_index+=2
        else:
            result[neg_index] = nums[i]
            neg_index+=2    
    return result
print(Rearrange_element())    


# tc = o(n)
# sc = o(1)   


 