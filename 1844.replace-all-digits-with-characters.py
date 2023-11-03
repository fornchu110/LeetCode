#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
# 給一串字串, a1的話回傳ab, 也就是a和a後面一個字母b, x0回傳xx, 以此類推
# Ex: "a1b2c3d4e"轉換成"abbdcfdhe"

# By string proccessing, time: O(n), space: O(n)
# space: O(n)是因python不能直接依序修改字串, 不好處理所以用一個arr list再做轉換多花空間
# 若用c或c++直接處理就是O(1)
class Solution:
    def replaceDigits(self, s: str) -> str:
        n = len(s)
        arr = list(s)
        # 偶數位置的字元必定是重複的, 看奇數位置的字元知道和偶數位置字元之相對位置即可
        for i in range(1, n, 2):
            arr[i] = chr(ord(arr[i-1])+int(arr[i]))
        return "".join(arr)

# @lc code=end

