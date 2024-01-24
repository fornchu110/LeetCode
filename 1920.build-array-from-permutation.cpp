/*
 * @lc app=leetcode id=1920 lang=cpp
 *
 * [1920] Build Array from Permutation
 */

// @lc code=start
// C++ Core Guildlines練習

class Solution
{
public:
    vector<int> buildArray(vector<int>& nums)
    {
        // 宣告內容為int的vector並靜態配置記憶體避免無謂的動態記憶體分配
        vector<int> res;
        res.reserve(nums.size());
        
        // 能用range-based for loop就用, 避免index錯誤
        // 
        for(const auto& num : nums)
        {
            // num就是nums[i], 所以直接迭代就好不需要index-based for loop
            // emplace_back代替push_back效能較好
            res.emplace_back(nums[num]);
        }

        return res;
    }
};
// @lc code=end

