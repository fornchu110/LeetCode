<<<<<<< HEAD
#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
# By bitwise XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
    
# By hashtable
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         hashTable = dict()
#         for i in range(len(nums)):
#             if nums[i] in hashTable:
#                 hashTable[nums[i]]+=1
#             else:
#                 hashTable[nums[i]] = 1
#         for i in range(len(nums)):
#             if hashTable[nums[i]]==1:
#                 return nums[i]
#         return 0

# @lc code=end

=======
#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
# By bitwise XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
    
# By hashtable
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         hashTable = dict()
#         for i in range(len(nums)):
#             if nums[i] in hashTable:
#                 hashTable[nums[i]]+=1
#             else:
#                 hashTable[nums[i]] = 1
#         for i in range(len(nums)):
#             if hashTable[nums[i]]==1:
#                 return nums[i]
#         return 0

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
