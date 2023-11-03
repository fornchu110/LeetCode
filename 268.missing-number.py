#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number

# @lc code=start
# 有範圍0~n, 給一陣列nums, nums長度會是n且元素都unique, 找出0~n中(n+1個元素)缺少的那一元素

# By bitwise(XOR), time: O(n), space: O(1)
# nums有n個元素, 若在nums後添加0~n這n+1個元素, 這樣總共就有2n+1個元素
# 這2n+1個元素中, 只有缺少的那一元素出現一次, 其他沒缺少的元素都出現了兩次
# 所以這2n+1個元素全部一起做XOR, 最後就會是缺失的那一元素, 因沒缺失的XOR後=0, 而0和缺失的XOR即是缺失的
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        # 對2n個元素做XOR, 其中i要代表的是後來添加的0~n這n+1個
        for i, num in enumerate(nums):
            xor ^= i^num
        # 但因nums只有n個, 上面i只代表0~n-1
        # 還缺少一個後來增加的元素, 即是n, 也就是len(nums)
        # 這樣就將2n+1個元素都互相做XOR得出結果
        return xor^len(nums)

# By hash, time: O(n), space: O(n)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         # 因nums元素不重複, 且set()可以用in當作hash查找, 所以用set(nums)建立hash
#         hash = set(nums)
#         # 因nums必定已經缺少一個, 所以找len(nums)+1個index, 也就是從0找到len(nums)
#         for i in range(len(nums)+1):
#             # 不在hash內的index就代表缺失了
#             if i not in hash:
#                 return i

# By sort and index, time: O(nlogn), space: O(logn)
# space = O(logn)的原因是.sort()在recursive時占用的stack空間
# 先將nums排序過後, 檢驗是否和index相同, 不同就代表少了index, 直到最後都相同就代表少了index+1
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         res = 0
#         for i in nums:
#             if i!= res:
#                 return res
#             res += 1
#         # 當發現從頭走訪到尾都和index相同, 代表其實是index+1這個元素缺失了
#         # Ex: nums = [0,1], 而答案就是2
#         return res
        
# @lc code=end

