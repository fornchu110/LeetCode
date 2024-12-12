/*
 * @lc app=leetcode id=1768 lang=cpp
 *
 * [1768] Merge Strings Alternately
 */

// @lc code=start
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string res = "";
        auto max_len = std::max(word1.length(), word2.length());
        int i;

        for (i = 0; i < max_len; i++) {
            if (i < word1.length()) {
                res += word1[i];
            }

            if (i < word2.length()) {
                res += word2[i];
            }
        }

        return res;
    }
};
// @lc code=end

