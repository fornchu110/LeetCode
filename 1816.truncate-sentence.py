#
# @lc app=leetcode id=1816 lang=python3
#
# [1816] Truncate Sentence
#

# @lc code=start
# By string processing, time: O(n), space: O(1), n=len(str)
# �n�Dreturn���w�y�ls���ek�ӳ�r
# �Q��split��y�l���������P��r��blist��, k�H���Nappend��res
# �̫�Nres��" ".join()���覡�qlist�ܦ^�@�ӥy�l�r��
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = []
        for idx, i in enumerate(s.split()):
            if idx<k:
                res.append(i)
        return " ".join(res)

# By index, time: O(n), space: O(1)
# ���Xs�����r��, �Q�ιJ��Ů�ε����P�_�@�ӳ�r��������oindex
# �̫�return�}�Y��index����s
# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         cnt = 0
#         for i in range(1, len(s)+1):
#             if i==len(s) or s[i]==" ":
#                 cnt += 1
#                 if cnt==k:
#                     end = i
#                     break
#         return s[:end]
                    
# @lc code=end

