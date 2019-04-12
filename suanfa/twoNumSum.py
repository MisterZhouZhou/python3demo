import time

# 1、效率比较低
# time:6.9141387939453125e-06
'''
class Solution(object):
    def twoSum(self,nums, target):
        l = len(nums)
        for a in range(l):
            for b in range(l):
                if a != b:
                    if nums[a] + nums[b] == target:
                        return [a,b]
'''

# 2、效率比较低
# time: 3.528594970703125e-05
'''
class Solution(object):
    def twoSum(self,nums, target):
        l = len(nums)
        for a in range(l):
            for b in range(a+1,l):
                if nums[a] + nums[b] == target:
                    return [a,b]
'''


# 3、效率一般
# time: 1.3113021850585938e-05
'''
class Solution(object):
    def twoSum(self,nums, target):
        flags = [0,0,0,0]
        l = len(nums)
        for a in range(l):
            flags[a] = 1
            for b in range(l):
                if flags[b] == 0:
                   if nums[a] + nums[b] == target:
                    return [a,b]
'''


# 4、效率一般
# time: 1.3113021850585938e-05
'''
class Solution(object):
    def twoSum(self,nums, target):
        l = len(nums)
        for a in range(l):
            one_num = nums[a]
            other_num = target - one_num
            if other_num in nums:
                b = nums.index(other_num)
                if a != b:
                    if a>b:
                        return [b,a]
                    return [a,b]
'''


# 5、效率很好
# time: 1.3113021850585938e-05
class Solution(object):
    def twoSum(self,nums, target):
        l = len(nums)
        dict_nums = {nums[i]:i for i in range(l)}
        for a in range(l):
            one_num = nums[a]
            other_num = target - one_num
            if other_num in dict_nums and a != dict_nums[other_num]:
                return [a, dict_nums[other_num]]



if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    test_o = Solution()
    start_time = time.time()
    result = test_o.twoSum(nums, target=target)
    end_time = time.time()
    print(end_time-start_time)