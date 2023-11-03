#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
# By by index, time: O(n), space: O(1)
# items都依據[type, color, name]格式存資訊, 求與給定key相同value的items數量
# 可以看到固定把type存在index 0, color存在index 1, name存在index 2, 以此當index去判斷value
# c語言的字串相等就是用strcmp()==0判斷, 這是自己像c語言得寫法
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for i in items:
            if ruleKey=="type":
                if i[0]==ruleValue:
                    cnt += 1
            elif ruleKey=="color":
                if i[1]==ruleValue:
                    cnt += 1
            else:
                if i[2]==ruleValue:
                    cnt += 1
        return cnt

# By hash, time: O(n), space: O(1)
# python可以用更簡潔快速的做法
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         # 當ruleKey為不同時, 給不同index
#         index = {"type": 0, "color": 1, "name": 2}[ruleKey]
#         # 看item內index位置是否與ruleValue一樣, 用sum()加總
#         # 因為==是布林, 只會返回1(True)或0(False), 所以sum()就等同==的數量
#         return sum(item[index] == ruleValue for item in items)

# @lc code=end

