def right_rotate():
    
 nums = [3,9,5,6,7,2]
 print("original list :" , nums)
 n = len(nums)
 k = 10
 rotions = k%n
 for _ in range(0,rotions):
    e = nums.pop()
    nums.insert(0,e)
    print("rotated list:", nums)
 right_rotate()  

# tc = o(r*n)
# sc = o(1)


# better solution


def right_rotate():
 nums = [3,9,5,6,7,2,10,11]
 print("original list :" , nums) 
 n = len(nums)
 k = 5
 k = k%n
 nums [:] = nums[n-k:] + nums[:n-k]
 print("rotated list:", nums)
right_rotate()


# tc = o(n)
# sc = o(1)


# optimal solution

def reverse(nums ,left,right):
    while left<right:
         nums[left],nums[right] = nums[right],nums[left]
         left +=1
         right -=1
nums = [3,9,5,6,7,2,10,11]
print("original list :" , nums) 
n = len(nums)
k= 5
# reverse last k element
reverse(nums,n-k,n-1)
# reverse first n-k elements
reverse(nums,0,n-k-1)
# reverse the entire list 
reverse(nums,0,n-1)

print("rotated list:", nums)

    #  tc = o(n)
    # sc = o(1)