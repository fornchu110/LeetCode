#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
# 給一字串, 只比較alphanumeric character是否迴文, 也就是字母和數字
# 注意一個字母的大小寫算同一種

# By double pointer and isalnnum(), time: O(n), space: O(1)
# isalnum()判斷字母和數字, isalpha()判斷字母
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            # 不使用if和continue就在not前面加個while l<r and 
            # 將非alphanumeric character
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            # 走到這代表是alnum, 若經過lower卻不相等return False
            if s[l].lower()!=s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

# By isalnum() and lower and[::-1], time: O(n), space: O(n)
# 利用isalnum()判斷字元是否是alphanumeric character, 是的話用lower()轉換成小寫加入res內
# 最後判斷res是否等同從res[::-1]即可
# 優化成space = O(1)的話就要在原字串s做判斷, 但一樣是用isalnum()和lower, 只是必定要用double pointer
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         res = []
#         for i in s:
#             if i.isalnum():
#                 # 數字和小寫不會被.lower()轉換, 只有大寫才被影響
#                 # 這邊用.upper()也是同理
#                 res.append(i.lower())
#         res = "".join(res)
#         # 上面的一行寫法, 列表生成式
#         # res = "".join(ch.lower() for ch in s if ch.isalnum())
#         return res==res[::-1]

# By double pointer and ord(), time : O(n), space: O(1)
# 從頭端和尾端分別判斷當下指向的alphanumeric characters是否符合迴文要求
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l = 0
#         r = len(s)-1
#         while l<r:
#             if not (ord('a')<=ord(s[l])<=ord('z') or ord('A')<=ord(s[l])<=ord('Z') or ord('0')<=ord(s[l])<=ord('9')):
#                 l += 1
#                 continue
#             elif not (ord('a')<=ord(s[r])<=ord('z') or ord('A')<=ord(s[r])<=ord('Z') or ord('0')<=ord(s[r])<=ord('9')):
#                 r -= 1
#                 continue
#             if ord('a')<=ord(s[l])<=ord('z'):
#                 print('1')
#                 if not (ord(s[l])==ord(s[r]) or ord(s[l])==ord(s[r])+32):
#                     print(s[l], s[r])
#                     return False
#                 else:
#                     l += 1
#                     r -= 1
#             elif ord('A')<=ord(s[l])<=ord('Z'):
#                 if not (ord(s[l])==ord(s[r]) or ord(s[l])==ord(s[r])-32):
#                     print(s[l], s[r])
#                     return False
#                 else:
#                     l += 1
#                     r -= 1
#             elif ord('0')<=ord(s[l])<=ord("9"):
#                 if ord(s[l])!=ord(s[r]):
#                     print(s[l], s[r])
#                     return False
#                 else:
#                     l += 1
#                     r -= 1
#         return True
        
# @lc code=end

