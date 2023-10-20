#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start

# By divide array and dp, time: O(n), space: O(1)
# �D�Nindex�H�~�Ҧ�1���ʨ�index�ҭn�᪺����, �@���u�ಾ��1��index
# �o���D�إi�H�Q�n�ݥ����M�k��, ���D�X�H0��index���k���A�䨫�X���X����
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # ��Uindex������left��1, �k����right��1
        left, right, operations = int(boxes[0]), 0, 0
        # �����X�@�����Dindex 0(�_�l��m)�k�䦳�X��1
        for i in range(1, len(boxes)):
            if boxes[i] == '1':
                # �ݨ�@��1�N+1
                right += 1
                # ��ڤW���ʨ�0�����ƴN�Oindex�B
                # Ex: 4����0�n��4�B
                operations += i
        # res[0]�N�O����X��operations
        res = [operations]
        # �A���X�@��
        for i in range(1, len(boxes)):
            # �C���X�@��index, �Ҫ᪺�B�ƴN�|-�k��1���ƶq+����1���ƶq
            operations += left - right
            res.append(operations)
            if boxes[i] == '1':
                # �C���@��index�J��1, �N��U�@��index�k���|�֤@��1, �����|�h�@��1
                left += 1
                right -= 1
        return res

# By for loop, time: O(n^2), space: O(1)
# �ɤO��, �C����@��index���q�Y��
# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         res = list()
#         for i in range(len(boxes)):
#             s = sum(abs(j - i) for j, c in enumerate(boxes) if c == '1')
#             res.append(s)
#         return res
# @lc code=end

