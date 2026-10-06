# brute force solution
nums = [55,32,97,-55,45,56,36,88]
nums.sort()
print( nums[-2])

nums = [55,32,97,-55,45,56,36,88]
nums.sort()
n = len(nums)
print( nums[n-2])

# tc = o(N log N)
# sc = o(1)

# better solution

nums = [55,32,97,-55,45,56,36,88]
largest = float("-inf")
s_largest = float("-inf")
n = len(nums)
for i in range(0,n):
    largest = max(largest, nums[i])
for i in range(0,n):
    if nums[i]>s_largest and nums[i]!= largest:
        s_largest = nums[i]
print(s_largest)        
         
        #  tc = o(N+N) =o(2N)= o(n)
        # sc = o(1)
    #   optimal solution   
nums = [55,32,97,-55,45,56,36,88]
largest = float("-inf")
s_largest = float("-inf")
n = len(nums)
for i in range(0,n):
    if nums[i]>largest:
        s_largest = largest  
        largest = nums[i]
    elif nums[i]>s_largest and nums[i]!= largest:
        s_largest=nums[i]
print(s_largest)                 
        