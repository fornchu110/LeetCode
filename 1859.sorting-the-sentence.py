#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
# By split, time: O(n), space: O(n), n�O�r��s������
# �n�N�y�l�̷Ӹ̭��r�괣�Ѫ�idx���Ƨ�
class Solution:
    def sortSentence(self, s: str) -> str:
        # split()�N�r���ഫ��list�åH�ťդ��jlist������
        s = s.split()
        # �y�l���r�ꪺ�ƶq
        n = len(s)  
        # ��l��res, �]���n���Oindex array�Q�λݭn���ؤj�p��n��list
        # res = [0]*n�]���@�ˮĪG, ���v�T
        res = ["" for i in range(n)] 
        # �q�Y���X, �ˬd�C�Ӧr�괣�Ѫ��Ʀr�����s�Jres��index, �]�O1�}�l�ҥH�n-1
        # Ex: This1��Jres[0]
        for i in s:
            # i[:-1]�Opython������, �e���O�����϶�, �᭱�O���}�϶�
            # �ҥH-1��H���O�˼ƲĤ@�Ӥ�����ڤW�O���˼ƲĤG��
            # Ex: i = This1, i[:-1] = This
            # ��i��index��ڤW�li[-1]�]�N�O�˼ƲĤ@�Ӫ���m����
            # i[1]-1�N�O�]�W������, ���Ѫ�index�q1�}�l��res�q0�}�l
            res[int(i[-1])-1] = i[:-1]
        # ��" ".join�Nres�qlist�ഫ��str��return
        # �]�y�l�����r��|�H�ťն��j, �ҥH�O" "
        return " ".join(res)
        
# @lc code=end

