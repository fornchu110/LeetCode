#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
# 判斷s內的括號是否valid

# By stack, time: O(n), space: O(n+6), n = len(s), 6 = pairs所做hash花的空間
# 用list實作stack, append來push, pop將尾端取出
class Solution:
    def isValid(self, s: str) -> bool:
        # 長度非偶數一定會非法
        if len(s)&1:
            return False    
        # 實際上是一個hash, {}所以是dict資料結構
        # 用hash的作法避免了一堆if else
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for ch in s:
            # 遇到)、]、}時將內容取出, 檢測到不合法配對直接return False
            # 只在遇到這上面三種時會判斷False, 所以對invalid判斷不完整, 無法走訪完直接return True
            if ch in pairs:
                #記得stack[-1]是檢測list中最後一個元素
                if not stack or stack[-1]!=pairs[ch]:
                    return False
                stack.pop()
            # 遇到(、[、{時做push
            else:
                stack.append(ch)
        # 走訪完後stack為空代表正確, 不為空代表錯誤, 所以用not
        # 上面走訪時的檢測無法檢測出碰到重複(、[、{的情況, 所以才要這樣
        return not stack
     
# @lc code=end

