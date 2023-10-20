#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
# ���@��push���ǰ}�Cpushed�Mpop���ǰ}�Cpopped, return stack�O�_�i�H�ӳo��}�C�����ǹB�@

# By list simulation, time: O(n), space: O(n)
# ������list����, �p�G���B�~��stack������pushed�Mpopped���ܪŶ�������O(1)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, popidx = [], 0
        for i in pushed:
            stack.append(i)
            # ��stack���ݩMpopped�ثe�npop�������ۦP�~��pop
            # stack[-1]�N�O����, �]�N�O�̫�@��append�i������
            # ������nwhile stack?�]����stack���Ů�stack[-1]�|out of range
            while stack and stack[-1]==popped[popidx]:
                stack.pop()
                # ��pop���\���N�n��U��pop����H
                popidx += 1
        # stack�ѤU���׬�0�N�����pop���\
        return len(stack)==0

# @lc code=end

