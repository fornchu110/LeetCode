<<<<<<< HEAD
#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#

# @lc code=start
# By string processing, time: O(n), space: O(1), n��garbage���r���ƶq
# ��X�q�Y(index = 0)�B�zG�BP�BM�Ҫ�O�ɶ�, �u�n�r�ꤺ����@�N��1�ɶ�, �qgarbage��index���ʨ�index+1��Otravel[index���ɶ�]
# �D�X�B�z��G�BP�BM��O�`�ɶ�
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res, g, m, p, idx = 0, 0, 0, 0, 0
        for idx , i in enumerate(garbage):
            res += len(i)
            # ��r���O�_�s�b�r�ꤺ���n��in, �ΰj�騫�X�����
            for j in i:
                if "M"==j:
                    m = idx
                elif "G"==j:
                    g = idx
                elif "P"==j:
                    p = idx
        for i in range(m):
            res += travel[i]
        for i in range(g):
            res += travel[i]
        for i in range(p):
            res += travel[i]
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#

# @lc code=start
# By string processing, time: O(n), space: O(1), n��garbage���r���ƶq
# ��X�q�Y(index = 0)�B�zG�BP�BM�Ҫ�O�ɶ�, �u�n�r�ꤺ����@�N��1�ɶ�, �qgarbage��index���ʨ�index+1��Otravel[index���ɶ�]
# �D�X�B�z��G�BP�BM��O�`�ɶ�
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res, g, m, p, idx = 0, 0, 0, 0, 0
        for idx , i in enumerate(garbage):
            res += len(i)
            # ��r���O�_�s�b�r�ꤺ���n��in, �ΰj�騫�X�����
            for j in i:
                if "M"==j:
                    m = idx
                elif "G"==j:
                    g = idx
                elif "P"==j:
                    p = idx
        for i in range(m):
            res += travel[i]
        for i in range(g):
            res += travel[i]
        for i in range(p):
            res += travel[i]
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
