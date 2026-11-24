# brute force
nums = [100,4,200,1,3,2,5,101,106,107,108,109,110,1]
n =len( nums)
max_count = 0
for i in range(0,n):
    num = nums[i]
    count = 1
    while num+1 in nums:
        count+=1
        num+=1
    max_count = max(max_count,count)
    
print(max_count)



# tc = o(n^2)
# sc = o(1)

# better solution
nums = [100,4,200,1,3,2,5,101,106,107,108,109,110,1]
n = len(nums)
last_smaller = {}
count = 0
for num in nums:
    last_smaller[num] = num-1
    count = 1
    while last_smaller[num] in last_smaller:
        count += 1
        num = last_smaller[num]
    max_count = max(max_count, count)

print(max_count)

# tc = o(n)
# sc = o(n)     


# optimal solution
nums = [100,4,200,1,3,2,5,101,106,107,108,109,110,1]
num_set = set(nums)
