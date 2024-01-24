/*
 * @lc app=leetcode id=1929 lang=cpp
 *
 * [1929] Concatenation of Array
 */

// @lc code=start

// C++ Core Guildlince練習
class Solution
{
public:
    vector<int> getConcatenation(vector<int>& nums)
    {
        // 宣告內容為int的res
        vector<int> res;
        // 用reserve避免沒必要的動態記憶體分配
        res.reserve(2 * nums.size());

        // 想成python for num in nums:
        // 迭代時用const避免修改內容, 用auto自動判斷元素型態簡潔, &來以reference看省下value copy
        // 要修改時也要用&迭代才能修改
        for(const auto& num : nums)
        {
            // 想成python list的res.append(), emplace_back比push_back好在省下copy
            res.emplace_back(num);
        }

        for(const auto& num : nums)
        {
            res.emplace_back(num);
        }

        return res;
    }
};
// @lc code=end

