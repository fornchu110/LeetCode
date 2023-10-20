#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
# ���@�Ӱ}�Csalary, �N�̤j�ȩM�̤p�ȥh����, return�ѤU�o�Ǥ����������Ȩè���p�ƫ�5��
# �ä��n�D�p���I, �@���~�t�b10^-5���褺�����

# By min() and max(), time: O(n), space: O(1)
# ������min()�Mmax()��̤j�̤p��, ���Nsalary�����[�`��o��̧Y�i
class Solution:
    def average(self, salary: List[int]) -> float:
        maxValue = max(salary)
        minValue = min(salary)
        total = sum(salary) - maxValue-minValue
        return total/(len(salary)-2)

# By sort and deque, time: O(n), space: O(n)
# �Q��collections.deque()�s�@����queue, �Nsort�᪺salary���ݩM�Y�ݤ���pop�X, �]�N�O�̤j�̤p��
# �A��ѤU�����[�`������, �å�round����p���I�᤭��
# class Solution:
#     def average(self, salary: List[int]) -> float:
#         salary.sort()
#         queue = collections.deque()
#         for i in salary:
#             queue.append(i)
#         queue.pop()
#         queue.popleft()
#         res = 0
#         for i in queue:
#             res += i
#         res /= len(queue)
#         # round�ĤG�ӰѼƬO�p���I���, �Y�nres��str��format(res, %.5f)
#         # res = round(res, 5)
#         return res
# @lc code=end

