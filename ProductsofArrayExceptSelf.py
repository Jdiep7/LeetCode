nums = [1,2,3,4]

output = [1]*len(nums)
prefix = 1
suffix = 1
for i in range(len(nums)):
    output[i] = prefix
    prefix *= nums[i]

for i in range(len(nums)-1, -1, -1):
    output[i] *= suffix
    suffix *= nums[i]
    

print(output)
            