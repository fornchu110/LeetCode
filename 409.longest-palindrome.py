#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
# ���r��s, return�r��s���o�Ǥ�����զ����̪��j��r�����
# �]�N�O���Φb�G���ᶶ��, �u�ݱƦC�զX���զ����j��
# Ex: abccccdd�̪���զ�dccaccd�o�@���׬�7���j��

# By hash and greedy, time: O(n), space: O(S), S��s�������ƪ��r������
# �`�N�i�঳�r��������ѦP�@�Ӥ����c��
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # res�O�̫ᵪ�ת��̪�����, hash�ΨӰO�����P�����X�{����
        res = 0
        hash = dict()
        # ���Xs�����C�Ӥ����X�{������
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        # �O��hash��hash.items()�P�ɨ��Xkey�Mvalue
        for key, value in hash.items():
            # ���ݭn�o��, �]���᭱��//2���ӴN�|��0�M1�ܦ�0, �A*2�]�O0
            # if value>=2:
            # value//2<<1�ӥh��value���h�l��1, Ex: c��3�Ӧ��j��u�ݭn2��
            res += value//2<<1
            # �γo�q�N����return�ᨺ��, �]���b��O�_��1�Ӥ�����j�夤���]�u�|��@��
            # �Ө��@���N�O�b�����X�{�_�ƭӷ�U���, �B�u�bres�����ƭӮɻݭn��
            # �٤U�@��for�j�骺�ɶ�
            if res&1==0 and value&1==1:
                res += 1
        return res
            # �P�ɱN��value�
            # hash[key] -= value//2<<1
        # ��hash.values()�u���Xvalue, �]�i�H��hash.keys()�u���Xkey
        # �̭��Ҧ�key��value���O0�N�O1
        # for value in hash.values():
            # �u�n�������ѤU�@��, �N�i�H���ӷ�j�奿����������
            # if value==1:
            #     return res+1
        
# @lc code=end

