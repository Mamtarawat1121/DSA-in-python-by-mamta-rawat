# brute force solution
nums = [1,2,0,4,5,3,0,0,6,7,1,0,8,9,0]
n = len(nums)
print("original list:", nums)
temp = []

for i in range(0,n):
    if nums[i] != 0:
        temp.append(nums[i])
a = len(temp)  
for i in range(0,a):
    nums[i] = temp[i]
for i in range(a,n):
    nums[i] = 0
print("list after moving zeroes to the end:", nums)    
              
        # tc = o(n)
        # sc = o(n)
        
        #  optimal solution


def moveZeroes(nums):    
        
 nums = [1,2,0,4,5,3,0,0,6,7,1,0,8,9,0] 
 print("original list:", nums)
 n = len(nums)        
 if len(nums) ==1:
  return
 i = 0
 while i<len(nums):
    if nums[i] ==0:
        break
    i +=1
 if i == len(nums):
    return
 j = i+1
 while j < len(nums):
    if nums[j] != 0:
        nums[i],nums[j] = nums[j],nums[i]
        i +=1
    j +=1    
 print("list after moving zeroes to the end:", nums)   
    
    # tc = o(n)
    # sc = o(1)

