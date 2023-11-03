#
# @lc app=leetcode id=1309 lang=python3
#
# [1309] Decrypt String from Alphabet to Integer Mapping
#

# @lc code=start
# 給一字串由1~9, 10#~26#所組成, 並分別對應a~i, j~z, 將字串轉換成對應字串
# Ex: "10#11#12"轉換成"jkab"

# By string proccessing, time: O(n), space: O(1)
class Solution:
    def freqAlphabets(self, s: str) -> str:
        def get(st):
            # 1對應到小寫a, 等同於將"1"轉換成ascii 97的"a", 所以是+96
            return chr(int(st)+96)
        # idx用來知道目前處理到的字串位址, 初始化字串res
        idx, res = 0, ""
        while idx<len(s):
            # 每次要先看後兩個字元是否為#, 來判斷是j~z還是a~i
            # Ex: 12和12#對應的不同, 分別是ab和l
            # 注意c語言也是用s[i+2], 畢竟記憶體位置
            if idx+2<len(s) and s[idx+2]=='#':
                res += get(s[idx:idx+2])
                idx += 2
            else:
                # 用+把字元連起來, c語言用strcat
                res += get(s[idx])
            idx += 1
        return res

# @lc code=end

