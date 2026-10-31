# brute force solution
nums = [9,6,4,2,5,7,8,1]
n = len(nums)

for i in range(0,n+1):
    if i not in nums:
        result = i
print(result)

# tc = o(n*n)
# sc = o(1)

# better solution


nums = [9,7,8,5,6,3,1,2,0]
print(sorted(nums))
n = len(nums)
a = {}
for i in range(0,n+1):
    a[i] = 0
for  num in nums:
    a[num]   = 1
for k ,v in  a.items():
    if v==0:
        result = k
print(result)        
        
        
        # tc = o(n)
        # sc = o(n)
        
        
        
        # optimal solution
nums = [9,7,8,5,6,3,1,2]

n = len(nums) + 1

result = n*(n+1)//2 - sum(nums)

print(result)

# tc o(n)
# sc = o(1)