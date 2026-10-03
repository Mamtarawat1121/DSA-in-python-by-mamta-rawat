# average case
nums = [5,8,1,6,9,2,4]
n = len(nums)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
    
    # time complexity = o(n(n+1))/2
    
    # best case
    
nums = [1,2,3,4,5,6,7,8]
n =len(nums)
for i in range(n-2,-1,-1):
   is_swap = False
   for j in range(0,i+1):
       if nums[j]>nums[j+1]:
          nums[j],nums[j+1] = nums[j+1],nums[j]
          is_swap = True
       
#  time complexity = o(n)
# Sc = o(1)          
 
       
         
    