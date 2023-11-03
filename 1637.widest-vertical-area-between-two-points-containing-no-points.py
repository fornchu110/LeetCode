<<<<<<< HEAD
#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
# �Hy�b�L�������Ӭ�, �^�Ǩ��I�����ϰ�S�����I���̼e�Z��
# ���N�O�ݨ��I����x�b�t�Z�̦h�h��

# By sort, time: O(nlogn), space: O(logn), �ƧǩҪ�O���Ŷ�
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # �Npoints�̭����I�ھ�x�b�ӱƧ�, �O��lambda�Ϊk
        # �n���q�{�����ѼƤ]�O��x[0]�ӱƪ�
        points.sort(key = lambda x: x[0])
        res = 0
        # �@�ӭӬݨ��I����x�b�t�Z, �̤j���N�O����
        for i in range(1, len(points)):
            res = max(res, points[i][0]-points[i-1][0])
        return res
            

# @lc code=end

=======
#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
# �Hy�b�L�������Ӭ�, �^�Ǩ��I�����ϰ�S�����I���̼e�Z��
# ���N�O�ݨ��I����x�b�t�Z�̦h�h��

# By sort, time: O(nlogn), space: O(logn), �ƧǩҪ�O���Ŷ�
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # �Npoints�̭����I�ھ�x�b�ӱƧ�, �O��lambda�Ϊk
        # �n���q�{�����ѼƤ]�O��x[0]�ӱƪ�
        points.sort(key = lambda x: x[0])
        res = 0
        # �@�ӭӬݨ��I����x�b�t�Z, �̤j���N�O����
        for i in range(1, len(points)):
            res = max(res, points[i][0]-points[i-1][0])
        return res
            

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
