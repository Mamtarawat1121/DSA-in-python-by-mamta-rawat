# Remove duplicate from sorted array[in place] 
# Brute force solution
def Remove_duplicates():
 nums = [1,1,1,2,3,4,4,5,6,7,7,8,9,9,9,10,11,44]
 print(nums)
 n = len(nums)
 frequancy_map = {}
 for i in range(0,n):
    frequancy_map[nums[i]] = 0
 j = 0
 for k in frequancy_map:
    nums[j] = k
    j +=1  
 return j  
print(Remove_duplicates())  

# Tc = o(2N) 
# sc = o(N)

# optimal solution
def Remove_duplicates():
 nums = [1,1,1,2,3,4,4,5,6,7,7,9,9,9,10,11,44]
 print(nums)
 n = len(nums)
 if n == 1:
     return 1
 i = 0
 j =i+1
 while j <n:
    if nums[j] != nums[i]:
        i +=1
        nums[i],nums[j]=nums[j],nums[i]
    j +=1
 return i + 1        
print(Remove_duplicates()) 

# tc = o(N)
# sc = o(1)





