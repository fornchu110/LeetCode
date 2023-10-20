#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
# 給一個push順序陣列pushed和pop順序陣列popped, return stack是否可以照這兩陣列的順序運作

# By list simulation, time: O(n), space: O(n)
# 直接用list模擬, 如果不額外建stack直接用pushed和popped的話空間複雜度O(1)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, popidx = [], 0
        for i in pushed:
            stack.append(i)
            # 當stack頂端和popped目前要pop的元素相同才能pop
            # stack[-1]就是頂端, 也就是最後一個append進的元素
            # 為什麼要while stack?因為當stack為空時stack[-1]會out of range
            while stack and stack[-1]==popped[popidx]:
                stack.pop()
                # 當pop成功那就要找下個pop的對象
                popidx += 1
        # stack剩下長度為0代表全部pop成功
        return len(stack)==0

# @lc code=end

