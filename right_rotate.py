def right_rotate():
    
 nums = [5,-2,3,9,6,10,7]
 print(nums)
 n = len(nums)
 temp = nums[n-1]
 for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
    
 nums[0] = temp
 return nums
print(right_rotate())





