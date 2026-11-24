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
nums.sort()
count = 0
last_smaller = ("-inf")
longest = 0
for num in range(0,n):
    num = nums[i]
    if num-1 == last_smaller:
        count+=1
        last_smaller = num
    elif num != last_smaller:
        count = 1
        last_smaller = num
    longest = max(longest, count)       
print(longest)    

# tc = o(n)
# sc = o(1)     


# optimal solution

nums = [100,4,200,1,3,2,5,101,106,107,108,109,110,1]
my_set = set()
for i in range(0,n):
    my_set.add(nums[i])
longest = 0
for num in my_set:
    if num - 1 not in my_set:
        x = num
        count = 1
        while x + 1 in my_set:
            x += 1
            count += 1
        longest = max(longest, count)
print(longest)

# tc = o(n)
# sc = o(n)