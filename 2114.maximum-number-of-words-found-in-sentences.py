#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
# By for loop, time: O(m), space: O(1), m�O���Ҧ�sentences���r���`��
# �|��Ҧ��r�ų��ݤ@�M, python��max()�Mcount()����
# ��X���wsentences����r�Ƴ̦h�����Өæ^�ǭ�
# ���i�H��C��sentence���ťռ�, �A+1�N�O��r��
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for i in sentences:
            cnt = 0
            # python�i�H�u�ΤU���o�ycount�ӭp��ťռ�
            # cnt = i.count(' ') + 1
            # ��sentence[i]���C�Ӧr��j�P�_�O�_���ť�
            for j in i:
                if j==" ":
                    cnt += 1
            # python�i�H����max(cnt, res)�Ӭݭ��Ӥ���j
            if cnt>res:
                res = cnt
        res += 1
        return res
        
# @lc code=end

