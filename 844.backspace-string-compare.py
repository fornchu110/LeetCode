#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
# ����r��s�Mt, �J��'#'�ɭn��backspace, �Bs�Mt���פ����o�ۦP, return �B�z������r��O�_�ۦP

# By stack, time: O(n+m), space: O(n+m), n = len(s), m = len(t)
# ����stack, �J��D#�Npush�istack(�D�ئ����u�|���p�g�^��r���M#), �J��#�Npop, �̫�ݬO�_�ۦP
# �i�H�o�{��s�M��t�O���P�˨Ʊ�, �o�D��²��g�k�ⰵ���Ʊ��g��function �ǤJs�M�ǤJt��
# �o�D�]�i�H��double popinter���Xs�Mt�Ӥ��ئ�stack�Ӱ�
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i1 in s:
            if ord('a')<=ord(i1)<=ord('z'):
                stack1.append(i1)
            elif i1=='#' and len(stack1):
                stack1.pop()
        for i2 in t:
            if ord('a')<=ord(i2)<=ord('z'):
                stack2.append(i2)
            elif i2=='#' and len(stack2):
                stack2.pop()
        return stack1==stack2
        
# @lc code=end

