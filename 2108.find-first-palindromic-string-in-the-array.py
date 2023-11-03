<<<<<<< HEAD
#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
# 找出給定words第一個迴文的字串

# By string proccessing, time: O(n), space: O(1), n = words中之字元數
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            # 注意reversed()返回的是迭代器, 要用list()接收成list或用"".join()接收成字串
            tmp = "".join(reversed(i))
            if tmp==i:
                return i
        return ""

# By double pointerm time: O(n), space: O(1)
# 不使用reversed()的作法, c語言也是這樣寫
# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         # 用一個函式判斷當下字串是否迴文
#         def isPalindrome(word: str) -> bool:
#             n = len(word)
#             # 從字串頭尾放置一個pointer, 確認頭尾是否相同
#             l, r = 0, n - 1
#             while l < r:
#                 # 中途字元不相同代表沒迴文
#                 if word[l]!=word[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             # 跑完字串仍沒return false代表迴文
#             return True
        
#         # ?序遍?字符串??，如果遇到回文字符串?返回，未遇到?返回空字符串
#         for i in words:
#             if isPalindrome(i):
#                 return i
#         # 走訪完代表沒找到迴文字串
#         return ""
        
# @lc code=end

=======
#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
# 找出給定words第一個迴文的字串

# By string proccessing, time: O(n), space: O(1), n = words中之字元數
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            # 注意reversed()返回的是迭代器, 要用list()接收成list或用"".join()接收成字串
            tmp = "".join(reversed(i))
            if tmp==i:
                return i
        return ""

# By double pointerm time: O(n), space: O(1)
# 不使用reversed()的作法, c語言也是這樣寫
# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         # 用一個函式判斷當下字串是否迴文
#         def isPalindrome(word: str) -> bool:
#             n = len(word)
#             # 從字串頭尾放置一個pointer, 確認頭尾是否相同
#             l, r = 0, n - 1
#             while l < r:
#                 # 中途字元不相同代表沒迴文
#                 if word[l]!=word[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             # 跑完字串仍沒return false代表迴文
#             return True
        
#         # ?序遍?字符串??，如果遇到回文字符串?返回，未遇到?返回空字符串
#         for i in words:
#             if isPalindrome(i):
#                 return i
#         # 走訪完代表沒找到迴文字串
#         return ""
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
