#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
# 給一陣列target和int n, 走訪1~n 用stack操作做出的跟target內容相同的陣列, return stack操作過程
# 結論就是無論走訪到誰都要push, 但只要和target完全一樣就return, 不一樣就pop, 除此之外直接走訪到下一個

# By double pointer, time: O(n), space: O(1)
# 省下用list的空間模擬的做法, 一一比對
# 利用while迴圈走訪n, 同時設定target檢測到最後一個後idx2+=1會==len(target)跳出迴圈
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        idx1 = 0
        idx2 = 0
        res = []
        while idx1<n and idx2<len(target):
            idx1 += 1
            res.append("Push") 
            if idx1==target[idx2]:
                idx2 += 1
            else:
                res.append("Pop")
        return res

# By double pointer, time: O(n), space: O(1)
# for迴圈版本
# class Solution:
#     def buildArray(self, target: List[int], n: int) -> List[str]:
#         idx2 = 0
#         res = []
#         for i in range(1, n+1):
#             res.append("Push")
#             if i==target[idx2]:
#                 idx2 += 1
#                 if(idx2)>=len(target):
#                     break
#             else:
#                 res.append("Pop")
#         return res

# By list simulation , time: O(n), space: O(n)
# 用list模擬stack操作
# class Solution:
#     def buildArray(self, target: List[int], n: int) -> List[str]:
#         stack = []
#         res = []
#         for i in range(1, n+1):
#             stack.append(i)
#             res.append("Push")
#             print(stack, target)
#             if stack==target:
#                 return res
#             if i not in target:
#                 stack.pop()
#                 res.append("Pop")
#             else:
#                 if stack==target:
#                     return res
#         return res
# @lc code=end

