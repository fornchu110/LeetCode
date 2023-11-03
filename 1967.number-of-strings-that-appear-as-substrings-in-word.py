<<<<<<< HEAD
#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
#

# @lc code=start

# By enumerate, time: O(n*m), space: O(1), n = len(word), m = patterns�r����
# �o�O�μɤO�k
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def check(pattern: str, word: str) -> bool:
            m = len(pattern)
            n = len(word)
            for i in range(n-m+1):
                flag = True
                for j in range(m):
                    if word[i+j]!=pattern[j]:
                        # ��o�{���i��Osubstring, flag��False�ô����������
                        flag = False
                        break
                # flag��True�N��ثe��pattern�Osubstring
                if flag:
                    # return True�N���Preturn 1
                    return True
            return False
        
        res = 0
        for pattern in patterns:
            # check�ΨӧP�_pattern�O�_��word��substring
            # c�y��<string.h>����strstr()�i�H�����P�_�O�_��substring
            res += check(pattern, word)
        return res

# By KMP
# �٤���, ��28�D�]�O, �����
# class Solution:
#     def numOfStrings(self, patterns: List[str], word: str) -> int:
#         def check(pattern: str, word: str) -> bool:
#             m = len(pattern)
#             n = len(word)
#             # �ͦ� pattern ���e???
#             pi = [0] * m
#             j = 0
#             for i in range(1, m):
#                 while j and pattern[i] != pattern[j]:
#                     j = pi[j - 1]
#                 if pattern[i] == pattern[j]:
#                     j += 1
#                 pi[i] = j
#             # �Q�Ϋe????��ǰt 
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

# By enumerate, time: O(n*m), space: O(1), n = len(word), m = patterns�r����
# �o�O�μɤO�k
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def check(pattern: str, word: str) -> bool:
            m = len(pattern)
            n = len(word)
            for i in range(n-m+1):
                flag = True
                for j in range(m):
                    if word[i+j]!=pattern[j]:
                        # ��o�{���i��Osubstring, flag��False�ô����������
                        flag = False
                        break
                # flag��True�N��ثe��pattern�Osubstring
                if flag:
                    # return True�N���Preturn 1
                    return True
            return False
        
        res = 0
        for pattern in patterns:
            # check�ΨӧP�_pattern�O�_��word��substring
            # c�y��<string.h>����strstr()�i�H�����P�_�O�_��substring
            res += check(pattern, word)
        return res

# By KMP
# �٤���, ��28�D�]�O, �����
# class Solution:
#     def numOfStrings(self, patterns: List[str], word: str) -> int:
#         def check(pattern: str, word: str) -> bool:
#             m = len(pattern)
#             n = len(word)
#             # �ͦ� pattern ���e???
#             pi = [0] * m
#             j = 0
#             for i in range(1, m):
#                 while j and pattern[i] != pattern[j]:
#                     j = pi[j - 1]
#                 if pattern[i] == pattern[j]:
#                     j += 1
#                 pi[i] = j
#             # �Q�Ϋe????��ǰt 
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
