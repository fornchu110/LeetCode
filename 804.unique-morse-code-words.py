#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
# By string proccessing, time: O(n), space: O(n), n��len(words)
# �Nwords���C�Ӧr���ഫ���K�X��, ��X�o�Ǧr�ꤣ���ƪ��ƶq
# �䤣���ƴN�n�Q��set(), ��len(set)�Y�O�����Ƽƶq
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for i in words:
            tmp = ""
            for j in i:
                # �Q��"a"+"b" = "ab", �bstring��+=���P�@�r�ꤺ���P�K�X�s���A�@�_
                # c�y���O�ϥ�sprinf()���s��, �z�L�n�B�z���r�ũҦb��}�Ӱ�
                tmp += code[ord(j)-ord("a")]
            # �C���N�B�z�����r��[�ires, �`�Nset�O��.add()���Oappend
            res.add(tmp)
        return len(res)
        # �W�����q���@�檩, ���ݤ����p����ഫ�L���r��join��
        # return len(set("".join(code[ord(ch) - ord('a')] for ch in word) for word in words))

# @lc code=end

