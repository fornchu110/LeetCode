<<<<<<< HEAD
#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
# ������a�Bb, ��+�M-�H�~���覡���Xa+b
# ���[�Q��bitwise�B��, �[��a+b���ʽ�

# @lc code=start
# By bitwise, time: O(log(max_int)), space: O(1)
# �`�N���X�@�Ӽ�n�Ҧ�bit���ɶ������׬�log(n)
# �b�G�i��P�@��Ʊ��p, a+b�����G��굥�PXOR, �u�O�b1+1�ɭn�h�B�z�@�Ӷi��
# Ex: 0+0=0, 0+1=1, 1+0=1, 1+1=0
# ����򪾹D���Ǧ�ƭn�i��?�[��o���P��ƤU, AND�ᬰ1�~�|�O�n�i�쪺��
# Ex: 0&0=0, 0&1=0, 1&0=0, 1&1=1
# �ҥH�Na+b������L�i�쪺���G�M���i�쪺���G

# �`�Npython����������O�L����, �ҥH�n��MASK���B�~�B�z�ܦ^32bit�ɪ��ˤl
# �ܦ^32bits�ɪ��ˤl�N��overflow�N��overflow
# ��MASK1��mod�u�ѤU����2^32����, �]�N�O���ѤU��32��bit
# c�y����unsigned int�B�z
MASK1 = 4294967296  # 2^32, ���P��0x100000000 (1 0000 0000 0000 0000 0000 0000 0000 0000)
MASK2 = 2147483648  # 2^31, ���P��0x80000000(1000 0000 0000 0000 0000 0000 0000 0000)
MASK3 = 2147483647  # 2^31-1, ���P��0x7FFFFFFF(0111 1111 1111 1111 1111 1111 1111 1111)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        a %= MASK1
        b %= MASK1
        # Ex: a=5(0101), b=4(0100), 
        # ����S���i��n�B�z�~�N��W����a = a^b���P��ڤW��a+b
        while b!=0:
            # �ݭn���ˬd���Ǧ�ƭn�i��
            # a&b�N��n�i�쪺��, <<1�᪺carry�N�N��i��L�᪺���G
            # Ex: �Ĥ@��a&b=0100, a&b<<1=1000
            # Ex: �ĤG��a&b=1000&0001=0, carry=0, �ҥH�b�o���N�|����
            carry = ((a&b)<<1)%MASK1
            # ��a�B�z���g�L���i��[�k�᪺�ˤl, ���P�󰵥[�k
            # Ex: �Ĥ@��a^b=0001
            # EX: �ĤG��a^b=0001^1000=1001, �]�N�O9, ��a�x�s�_��
            a = (a^b)%MASK1
            # b�ܦ��i��L�᪺���G����
            # Ex: �Ĥ@��b=1000
            # Ex: �ĤG��b=carry=0, �Y�N�����j��
            b = carry
        # �ҥH�����j���, �Ya�O���ƨ��N�O��ڤW������
        # �⵲�G����^�hpython���, input���t�ƩҥH���G�]�i��O�t��
        # ����32bit int�O-2^31~2^31-1, ��2^31�N��۲�32��bit
        # �ҥH��M2^31��&�D0��, �N���32��bit��1, �]�N�O�t��
        if a&MASK2:
            # �ѩ�e���u���F�t�ƪ���32bit���B��, �n�ഫ�^�h
            # Ex: ���]8bit, ���Ga=-4�o�ɫo�|�o�X0000 1100, �ҥH�n�ഫ�^1111 1100
            # a^MASK2^MASK3���P��a^0xFFFFFFFF, �]�N�O2^32-1
            # ~(a^0xFFFFFFFF)���P�����32�줺�ন�ɼ�, �A����int�ন�ɼ�
            # �̫�32�줺�S��, ��32��H�~�ܦ�11..11, �~�|�ܦ����T�t��
            return ~(a^MASK2^MASK3)
        # ����, ����return a
        else:
            return a
        
# @lc code=end

=======
#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
# ������a�Bb, ��+�M-�H�~���覡���Xa+b
# ���[�Q��bitwise�B��, �[��a+b���ʽ�

# @lc code=start
# By bitwise, time: O(log(max_int)), space: O(1)
# �`�N���X�@�Ӽ�n�Ҧ�bit���ɶ������׬�log(n)
# �b�G�i��P�@��Ʊ��p, a+b�����G��굥�PXOR, �u�O�b1+1�ɭn�h�B�z�@�Ӷi��
# Ex: 0+0=0, 0+1=1, 1+0=1, 1+1=0
# ����򪾹D���Ǧ�ƭn�i��?�[��o���P��ƤU, AND�ᬰ1�~�|�O�n�i�쪺��
# Ex: 0&0=0, 0&1=0, 1&0=0, 1&1=1
# �ҥH�Na+b������L�i�쪺���G�M���i�쪺���G

# �`�Npython����������O�L����, �ҥH�n��MASK���B�~�B�z�ܦ^32bit�ɪ��ˤl
# �ܦ^32bits�ɪ��ˤl�N��overflow�N��overflow
# ��MASK1��mod�u�ѤU����2^32����, �]�N�O���ѤU��32��bit
# c�y����unsigned int�B�z
MASK1 = 4294967296  # 2^32, ���P��0x100000000 (1 0000 0000 0000 0000 0000 0000 0000 0000)
MASK2 = 2147483648  # 2^31, ���P��0x80000000(1000 0000 0000 0000 0000 0000 0000 0000)
MASK3 = 2147483647  # 2^31-1, ���P��0x7FFFFFFF(0111 1111 1111 1111 1111 1111 1111 1111)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        a %= MASK1
        b %= MASK1
        # Ex: a=5(0101), b=4(0100), 
        # ����S���i��n�B�z�~�N��W����a = a^b���P��ڤW��a+b
        while b!=0:
            # �ݭn���ˬd���Ǧ�ƭn�i��
            # a&b�N��n�i�쪺��, <<1�᪺carry�N�N��i��L�᪺���G
            # Ex: �Ĥ@��a&b=0100, a&b<<1=1000
            # Ex: �ĤG��a&b=1000&0001=0, carry=0, �ҥH�b�o���N�|����
            carry = ((a&b)<<1)%MASK1
            # ��a�B�z���g�L���i��[�k�᪺�ˤl, ���P�󰵥[�k
            # Ex: �Ĥ@��a^b=0001
            # EX: �ĤG��a^b=0001^1000=1001, �]�N�O9, ��a�x�s�_��
            a = (a^b)%MASK1
            # b�ܦ��i��L�᪺���G����
            # Ex: �Ĥ@��b=1000
            # Ex: �ĤG��b=carry=0, �Y�N�����j��
            b = carry
        # �ҥH�����j���, �Ya�O���ƨ��N�O��ڤW������
        # �⵲�G����^�hpython���, input���t�ƩҥH���G�]�i��O�t��
        # ����32bit int�O-2^31~2^31-1, ��2^31�N��۲�32��bit
        # �ҥH��M2^31��&�D0��, �N���32��bit��1, �]�N�O�t��
        if a&MASK2:
            # �ѩ�e���u���F�t�ƪ���32bit���B��, �n�ഫ�^�h
            # Ex: ���]8bit, ���Ga=-4�o�ɫo�|�o�X0000 1100, �ҥH�n�ഫ�^1111 1100
            # a^MASK2^MASK3���P��a^0xFFFFFFFF, �]�N�O2^32-1
            # ~(a^0xFFFFFFFF)���P�����32�줺�ন�ɼ�, �A����int�ন�ɼ�
            # �̫�32�줺�S��, ��32��H�~�ܦ�11..11, �~�|�ܦ����T�t��
            return ~(a^MASK2^MASK3)
        # ����, ����return a
        else:
            return a
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
