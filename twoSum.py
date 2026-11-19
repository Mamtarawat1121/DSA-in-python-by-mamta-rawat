# brute force
nums = [2,7,11,15,4,9,1,7]
target = 9
n = len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            result = [i,j]
print(result)

# tc = o(n*n)
# sc = o(1)


# optimal solution


nums = [7, 9, 0, 8, 2, 15, 4]
n = len(nums)
target = 13

hash_map = {}

def two_sum(nums, target):
    for i in range(len(nums)):
        remaining = target - nums[i]

        if remaining in hash_map:
            return [hash_map[remaining], i]

        else:
            hash_map[nums[i]] = i

    return []

print(two_sum(nums, target))
        #tc = o(n)
        #sc = o(n) 






















