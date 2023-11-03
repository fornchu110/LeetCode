#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start

# By counting sort, time: O(n+k), space: O(k), k是input值域大小
# 記住counting sort是線性排序很快, 但更花空間, 因為根據值域決定
# counting sort就是index array的想法, 把值本身當index
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 題目給input最多101個元素, 101也就是值域大小k
        arr = [0]*101
        res = list()
        # 在arr內紀錄0~101中於nums內出現的次數
        # 由於arr之index是nums內元素本身, 所以其實走訪arr就會由小至大走訪nums
        for i in nums:
            arr[i] += 1 
        lessthan = list()  
        # 就是arr內各個元素(index)當下的值
        temp = 0 
        # 走訪arr對temp做加總代表著
        # 由小至大看比當下元素更小之元素的出現次數和, 並加入lessthan之中
        # 所以lessthan的大小和arr一樣, 都是[0]*101
        for i in arr:
            # temp+=i在append之後, 所以不會算到當下元素自己的出現次數
            # 若要算<=次數就把temp+=i放到append前面
            lessthan.append(temp)
            temp += i
        # 以nums內之元素作為index查詢lessthan即可知道小於自己的元素數量
        for i in nums:  
            res.append(lessthan[i])
        return res

# By sort and hash, time: O(n*log(n)), space: O(n)
# 重點在於排序過後的nums內, 每個元素第一次出現的index即是小於他的元素數量
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         res = list()
#         hash = dict()
#         # nums.sort()直接將nums做排序, sorted(nums)則回傳一個新的list
#         # 在這邊由於需要照順序return, 所以需要用一個sort過的新list
#         arr = sorted(nums)
#         # 依序走訪排序過的arr
#         # 其實每元素第一次出現時的index就是小於該元素的元素數量
#         for i in range(len(arr)):
#             if arr[i] not in hash:
#                 hash[arr[i]] = i
#         # 已經用hash紀錄小於各元素的數量, 照nums的順序走訪一遍加入res
#         for i in nums:
#             res.append(hash[i])
#         return res
        
# @lc code=end

