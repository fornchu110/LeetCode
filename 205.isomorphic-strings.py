#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start

#By str process
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         return all(s.index(s[i]) == t.index(t[i])  for i in range(len(s)))

#這題目標只有s不要多對一
#By hashtable
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        if lens!=lent:
            return False
        hashtable1 = dict()
        #如果要用hashtable回頭找時建的
        # hashtable2 = dict()
        for i in range(lens):
            if s[i] in hashtable1:
                if hashtable1[s[i]]!=t[i]:
                    return False
            else:
                hashtable1[s[i]] = t[i]
                #每次有新的s[i]要加入時
                #回頭看有沒有i以前的s對應到同樣的t
                #可以用for迴圈回頭找或建另一個hashtable找
                #每次用for找,比較快?
                for j in range(i):
                    if hashtable1[s[j]]==t[i]:
                        return False            
                #用hash table找
                # if t[i] in hashtable2:
                #     if hashtable2[t[i]]!=s[i]:
                #         return False
                # hashtable2[t[i]] = s[i]
        return True

# @lc code=end