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

#�o�D�ؼХu��s���n�h��@
#By hashtable
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        if lens!=lent:
            return False
        hashtable1 = dict()
        #�p�G�n��hashtable�^�Y��ɫت�
        # hashtable2 = dict()
        for i in range(lens):
            if s[i] in hashtable1:
                if hashtable1[s[i]]!=t[i]:
                    return False
            else:
                hashtable1[s[i]] = t[i]
                #�C�����s��s[i]�n�[�J��
                #�^�Y�ݦ��S��i�H�e��s������P�˪�t
                #�i�H��for�j��^�Y��Ϋإt�@��hashtable��
                #�C����for��,�����?
                for j in range(i):
                    if hashtable1[s[j]]==t[i]:
                        return False            
                #��hash table��
                # if t[i] in hashtable2:
                #     if hashtable2[t[i]]!=s[i]:
                #         return False
                # hashtable2[t[i]] = s[i]
        return True

# @lc code=end

