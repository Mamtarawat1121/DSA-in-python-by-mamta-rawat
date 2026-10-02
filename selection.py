nums = [1,8,6,7,5,3,9,2]
def Selection_sort(nums):
   n = len(nums)
   for i in range(0,n):
     mini_index = i
   for j in range(i+1,n):
       if nums[j]<nums[mini_index]:
          mini_index = j
nums[i],nums[mini_index] = nums[mini_index],nums[i]