#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
# 給兩字串s和t, 遇到'#'時要做backspace, 且s和t長度不見得相同, return 處理完的兩字串是否相同

# By double pointer, time: O(n), space: O(1), n = max(len(s), len(t))
# 用double pointer分別從s和t的尾端開始走訪
# 如果遇到'#'再遇到字元就可以把他刪掉繼續走
# 如果還沒遇到"#"就遇到字元代表這個字元是處理完會實際被留下來的
class Solution:
    def processing(self, s, len):
        cnt = 0
        # 由後往前看, -1時代表字串會被刪光
        while len>=0:
            if s[len]=='#':
                cnt += 1
            elif cnt>0:
                cnt -= 1
            # 遇到字元又沒有'#'能把他刪掉
            else:
                break
            len -= 1
        return len

    def backspaceCompare(self, s: str, t: str) -> bool:
        slen = len(s)-1
        tlen = len(t)-1
        # 必須是or不是end才能在裡面得到1, 0後同時-=1變成0, -1這種狀況進去判斷
        # 能夠判斷這種狀況才算處理完
        while slen>=0 or tlen>=0:
            # processing回傳的是從後往前看無把被刪掉的字元所在index
            slen = self.processing(s, slen)
            tlen = self.processing(t, tlen)
            # 兩者都<0代表兩者的字串都在這輪被處理完了
            if slen<0 and tlen<0:
                return True
            # 有人沒被處理完但有人被處理完了
            if slen<0 or tlen<0:
                return False
            # slen和tlen照理來說都是第i個不會被刪掉的字元, 所以必須一樣
            elif s[slen]!=t[tlen]:
                return False
            # 走到這代表沒有人被處理完, 繼續往下處理, 不-1的話會無限迴圈
            slen -= 1
            tlen -= 1
        return True

# By stack simulation, time: O(n+m), space: O(n+m), n = len(s), m = len(t)
# 模擬stack, 遇到非#就push進stack(題目有說只會給小寫英文字母和#), 遇到#就pop, 最後看是否相同
# 可以發現對s和對t是做同樣事情, 這題更簡潔寫法把做的事情寫成function 傳入s和傳入t做
# 這題也可以用double popinter走訪s和t而不建成stack來做
# By stack, time: O(n+m), space: O(n+m), n = len(s), m = len(t)
# 模擬stack, 遇到非#就push進stack(題目有說只會給小寫英文字母和#), 遇到#就pop, 最後看是否相同
# 可以發現對s和對t是做同樣事情, 這題更簡潔寫法把做的事情寫成function 傳入s和傳入t做
# 這題也可以用double popinter走訪s和t而不建成stack來做
# class Solution:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
        
#     def processing(self, input, stack):
#         for i in input:
#             if ord('a')<=ord(i)<=ord('z'):
#                 stack.append(i)
#             elif i=='#' and len(stack):
#                 stack.pop()

#     def backspaceCompare(self, s: str, t: str) -> bool:
#         self.processing(s, self.stack1)
#         self.processing(t, self.stack2)
#         return self.stack1==self.stack2
        
# @lc code=end

# @lc code=end

