<<<<<<< HEAD
#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
# ��a, b���, return a, b�����]�Ƽƶq

# By simulation, time: O(min(a, b)), space: O(1)
# �u��1: ����a, b���������i��O���]��, �]���u�n���N��min(a, b)�H�U����
# �q1��min(a, b)����a�Mb�O�_���㰣, �]�N�O%0, ���߮�res+1
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        if a>b:
            tar = b
        else:
            tar = a
        for i in range(1, tar+1):
            if a%i==0 and b%i==0:
                res += 1
        return res
        
# @lc code=end

=======
#
# @lc app=leetcode id=2427 lang=python3
#
# [2427] Number of Common Factors
#

# @lc code=start
# ��a, b���, return a, b�����]�Ƽƶq

# By simulation, time: O(min(a, b)), space: O(1)
# �u��1: ����a, b���������i��O���]��, �]���u�n���N��min(a, b)�H�U����
# �q1��min(a, b)����a�Mb�O�_���㰣, �]�N�O%0, ���߮�res+1
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        if a>b:
            tar = b
        else:
            tar = a
        for i in range(1, tar+1):
            if a%i==0 and b%i==0:
                res += 1
        return res
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
