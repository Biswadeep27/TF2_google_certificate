#nums = [-2,1,-3,4,-1,2,1,-5,4]

#nums = [5,4,-1,7,8,-1]

nums = [-2,-1]

# length = len(nums)

i = 0
max_sum = nums[0]


while i<len(nums):
	j = i +1
	while j<=len(nums):
		print(f'i : {i}, j : {j}, list : {nums[i:j]}')
		if j < len(nums):
			if max_sum < sum(nums[i:j]):
				max_sum = sum(nums[i:j])
		if j == len(nums):
			if max_sum < sum(nums[i:]):
				max_sum = sum(nums[i:])
		j += 1
	i += 1

print(max_sum)