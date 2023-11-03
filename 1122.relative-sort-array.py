<<<<<<< HEAD
#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start

# By counting sort
# �ƥX�{���Ƭ����barray���A�̷ӭn�D���ǥ[�Jres 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # ��Xarr1�̤j���Ʀr
        upper = max(arr1)
        # �n�p��arr1���C�Ӥ����U�X�{�h�֦�
        # frequency[i]�N�Oi�o�ӼƦr�X�{������, �����Hi��index
        # array�̤֭n���̤j�Ʀr+1�Ӥj�p, �]���n�H�̤j�Ʀr��index
        # Ex:�̤j2, array�n���T�Ӥ����~��0, 1, 2
        frequency = [0]*(upper + 1)
        # ���Xarr1�C�Ӥ���x�}�l���W�v
        for x in arr1:
            frequency[x] += 1
        
        res = list()
        for x in arr2:
            # list.appen�[�J��Ӥ���, list.extend�@���[�J�h��
            # �Harr2�X�{�����ǱNfrequency[x]��x�[�Jres
            res.extend([x]*frequency[x])
            # frequency = 0�ΨӰO��arr2�����������Q�[�Jres�F
            frequency[x] = 0
        # �N�Ҧ�arr1���X�{�barr2���������[�Jres��    
        # ���୫�s��arr1�����X, ������frequency���X
        # ���M�̭��@�w�����ӴN�O�Ū�,�|���O�ɶ�
        # ��res�n�D�q�p��j�Ƨ�, �ӫD�ѤU������arr1�������ǱƴN�i�H
        for x in range(upper+1):
            # �u�nfrequency����0, �N��Oarr2�H�~������
            if frequency[x] > 0:
                # �N�L�̥[�Jres
                res.extend([x] * frequency[x])
        return res

# @lc code=end

=======
#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start

# By counting sort
# �ƥX�{���Ƭ����barray���A�̷ӭn�D���ǥ[�Jres 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # ��Xarr1�̤j���Ʀr
        upper = max(arr1)
        # �n�p��arr1���C�Ӥ����U�X�{�h�֦�
        # frequency[i]�N�Oi�o�ӼƦr�X�{������, �����Hi��index
        # array�̤֭n���̤j�Ʀr+1�Ӥj�p, �]���n�H�̤j�Ʀr��index
        # Ex:�̤j2, array�n���T�Ӥ����~��0, 1, 2
        frequency = [0]*(upper + 1)
        # ���Xarr1�C�Ӥ���x�}�l���W�v
        for x in arr1:
            frequency[x] += 1
        
        res = list()
        for x in arr2:
            # list.appen�[�J��Ӥ���, list.extend�@���[�J�h��
            # �Harr2�X�{�����ǱNfrequency[x]��x�[�Jres
            res.extend([x]*frequency[x])
            # frequency = 0�ΨӰO��arr2�����������Q�[�Jres�F
            frequency[x] = 0
        # �N�Ҧ�arr1���X�{�barr2���������[�Jres��    
        # ���୫�s��arr1�����X, ������frequency���X
        # ���M�̭��@�w�����ӴN�O�Ū�,�|���O�ɶ�
        # ��res�n�D�q�p��j�Ƨ�, �ӫD�ѤU������arr1�������ǱƴN�i�H
        for x in range(upper+1):
            # �u�nfrequency����0, �N��Oarr2�H�~������
            if frequency[x] > 0:
                # �N�L�̥[�Jres
                res.extend([x] * frequency[x])
        return res

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
