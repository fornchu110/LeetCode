<<<<<<< HEAD
#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
#

# @lc code=start

# By enumerate, time: O(n*m), space: O(1), n = len(word), m = patterns字元數
# 這是用暴力法
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def check(pattern: str, word: str) -> bool:
            m = len(pattern)
            n = len(word)
            for i in range(n-m+1):
                flag = True
                for j in range(m):
                    if word[i+j]!=pattern[j]:
                        # 當發現不可能是substring, flag為False並提早結束比對
                        flag = False
                        break
                # flag為True代表目前的pattern是substring
                if flag:
                    # return True就等同return 1
                    return True
            return False
        
        res = 0
        for pattern in patterns:
            # check用來判斷pattern是否為word的substring
            # c語言<string.h>內有strstr()可以直接判斷是否為substring
            res += check(pattern, word)
        return res

# By KMP
# 還不懂, 第28題也是, 之後看
# class Solution:
#     def numOfStrings(self, patterns: List[str], word: str) -> int:
#         def check(pattern: str, word: str) -> bool:
#             m = len(pattern)
#             n = len(word)
#             # 生成 pattern 的前???
#             pi = [0] * m
#             j = 0
#             for i in range(1, m):
#                 while j and pattern[i] != pattern[j]:
#                     j = pi[j - 1]
#                 if pattern[i] == pattern[j]:
#                     j += 1
#                 pi[i] = j
#             # 利用前????行匹配 
#             j = 0
#             for i in range(n):
#                 while j and word[i] != pattern[j]:
#                     j = pi[j - 1]
#                 if word[i] == pattern[j]:
#                     j += 1
#                 if j == m:
#                     return True
#             return False
        
#         res = 0
#         for pattern in patterns:
#             res += check(pattern, word)
#         return res

# @lc code=end

=======
#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
#

# @lc code=start

# By enumerate, time: O(n*m), space: O(1), n = len(word), m = patterns字元數
# 這是用暴力法
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def check(pattern: str, word: str) -> bool:
            m = len(pattern)
            n = len(word)
            for i in range(n-m+1):
                flag = True
                for j in range(m):
                    if word[i+j]!=pattern[j]:
                        # 當發現不可能是substring, flag為False並提早結束比對
                        flag = False
                        break
                # flag為True代表目前的pattern是substring
                if flag:
                    # return True就等同return 1
                    return True
            return False
        
        res = 0
        for pattern in patterns:
            # check用來判斷pattern是否為word的substring
            # c語言<string.h>內有strstr()可以直接判斷是否為substring
            res += check(pattern, word)
        return res

# By KMP
# 還不懂, 第28題也是, 之後看
# class Solution:
#     def numOfStrings(self, patterns: List[str], word: str) -> int:
#         def check(pattern: str, word: str) -> bool:
#             m = len(pattern)
#             n = len(word)
#             # 生成 pattern 的前???
#             pi = [0] * m
#             j = 0
#             for i in range(1, m):
#                 while j and pattern[i] != pattern[j]:
#                     j = pi[j - 1]
#                 if pattern[i] == pattern[j]:
#                     j += 1
#                 pi[i] = j
#             # 利用前????行匹配 
#             j = 0
#             for i in range(n):
#                 while j and word[i] != pattern[j]:
#                     j = pi[j - 1]
#                 if word[i] == pattern[j]:
#                     j += 1
#                 if j == m:
#                     return True
#             return False
        
#         res = 0
#         for pattern in patterns:
#             res += check(pattern, word)
#         return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
