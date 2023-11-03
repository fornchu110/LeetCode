<<<<<<< HEAD
#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start

#By hashtable
class Solution:
    #���Ƥ��U�Ӧ�ƥ���M
    def getNext(self, num):
        happy_sum = 0
        while num:
            happy_sum += (num % 10) ** 2
            num = num // 10
        return happy_sum

    #�ϥ������T�{�O�_�b�`��
    def isHappy(self, n: int) -> bool:
        hashTable = dict()
        while True:
            n = self.getNext(n)
            if n == 1:
                return True
            if n in hashTable:
                return False
            else:
                hashTable[n] = 1
        
# @lc code=end

=======
#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start

#By hashtable
class Solution:
    #���Ƥ��U�Ӧ�ƥ���M
    def getNext(self, num):
        happy_sum = 0
        while num:
            happy_sum += (num % 10) ** 2
            num = num // 10
        return happy_sum

    #�ϥ������T�{�O�_�b�`��
    def isHappy(self, n: int) -> bool:
        hashTable = dict()
        while True:
            n = self.getNext(n)
            if n == 1:
                return True
            if n in hashTable:
                return False
            else:
                hashTable[n] = 1
        
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
