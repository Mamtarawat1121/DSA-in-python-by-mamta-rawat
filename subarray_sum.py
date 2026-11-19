# brute force
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(nums)

max_sum = float('-inf')
for i in range(0, n):
    total = 0
    for j in range(i, n):
        total += nums[j]
        max_sum = max(max_sum, total)
print(max_sum)        
# tc = o(n*n)
# sc = o(1)




# optimal solution
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def max_subarray(nums):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum

print(max_subarray(nums))

# tc = o(n)
# sc = o(1)