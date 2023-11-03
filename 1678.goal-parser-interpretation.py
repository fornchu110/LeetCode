#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
# By for loop, time: O(n), space: O(1), 只需要一次走訪
# 記得用"".join(list)的方式將各元素為字串的list轉換成一個str
class Solution:
    def interpret(self, command: str) -> str:
        res = list()
        #enumerate用法前面是index後面是str[index], 也就是command[i]
        for i, c in enumerate(command):
            if c == 'G':
                res.append(c)
            elif c == '(':
                # 下面那段的一行寫法
                # res.append('o' if command[i + 1] == ')' else 'al')
                if command[i+1]==")":
                    res.append("o")
                else:
                    res.append("al")
        # join將res這個list內的str用''(也就是空白)連結, 成為一整個str
        # 也就是python中將list轉換成str的用法
        return ''.join(res)

# By replace, time: O(n), space: O(1), 因res是返回值不算在複雜度
# 利用python的replace功能做字串替換
# class Solution:
#     def interpret(self, command: str) -> str:
#         # str.replace("要被更改的舊字串", "被更改後的字串")
#         # 可以將一長串字串中的一部份做修改, 回傳改完的新字串
#         # 若沒接收回傳值, 舊字串不會做修改
#         # 不知為何res.command.replace("(al)", "al").replace("()", "o")會比較花時間
#         res = command.replace("(al)", "al")
#         res = res.replace("()", "o")
#         return res

# @lc code=end

