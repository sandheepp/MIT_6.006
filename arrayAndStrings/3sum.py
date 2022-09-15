def three_sum(nums):
    nums.sort()
    nums_set = list()
    length = len(nums)
    num_index = 0
    while(num_index<length):
        l = num_index
        r = length - 1
        while(num_index+1<length):
            if nums[num_index+1] == nums[num_index]:
                num_index+=1
            else:
                break
        while(l < r):
            if l == num_index:
                l = l+1
                continue
            if r == num_index:
                r = r-1
                continue

            if nums[l] + nums[r] == -nums[num_index]:
                new_list = [nums[l], nums[r], nums[num_index]]
                new_list.sort()
                if new_list not in nums_set:
                    nums_set.append(new_list)
                l = l+1
            elif nums[l] + nums[r] > -nums[num_index]:
                r-=1
            elif nums[l] + nums[r] < -nums[num_index]:
                l+=1
        num_index+=1
    return nums_set

nums = [0,1,2,3,4,-1,-2,-3,-4]
print(three_sum(nums))