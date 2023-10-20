#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
# 給兩字串s和t, 遇到'#'時要做backspace, 且s和t長度不見得相同, return 處理完的兩字串是否相同

# By stack, time: O(n+m), space: O(n+m), n = len(s), m = len(t)
# 模擬stack, 遇到非#就push進stack(題目有說只會給小寫英文字母和#), 遇到#就pop, 最後看是否相同
# 可以發現對s和對t是做同樣事情, 這題更簡潔寫法把做的事情寫成function 傳入s和傳入t做
# 這題也可以用double popinter走訪s和t而不建成stack來做
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i1 in s:
            if ord('a')<=ord(i1)<=ord('z'):
                stack1.append(i1)
            elif i1=='#' and len(stack1):
                stack1.pop()
        for i2 in t:
            if ord('a')<=ord(i2)<=ord('z'):
                stack2.append(i2)
            elif i2=='#' and len(stack2):
                stack2.pop()
        return stack1==stack2
        
# @lc code=end

