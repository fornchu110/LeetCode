#
# @lc app=leetcode id=2325 lang=python3
#
# [2325] Decode the Message
#

# @lc code=start
# By hash and ord() and chr(), time: O(m+n), space: O(26), m為key長度, n為message長度
# space: O(26)是因為hash用來儲存26個英文字母
# 給key從頭到尾分別對應a~z, 將message根據這個key變換出來
# 標準建hash表, 這題也可以用index array做表
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = list()
        # 用ord()來得到ascii code, 初始化為a
        ascii = ord('a')
        # 建對應的hash
        hash = dict()
        for i in key:
            # key內容有可以重複, 所以要判斷不在hash
            # 除了小寫英文只會有' '(空格)
            if i!=' ' and i not in hash:
                hash[i] = ascii
                # 按照第一次出現順序對應ascii
                # python沒辦法直接對字符做運算
                ascii += 1
        # 處理message
        for i in message:
            if i in hash:
                res.append(chr(hash[i]))
            else:
                res.append(' ')
        # 用''.join()將list轉換成字串
        return ''.join(res)

# @lc code=end

