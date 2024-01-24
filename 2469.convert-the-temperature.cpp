/*
 * @lc app=leetcode id=2469 lang=cpp
 *
 * [2469] Convert the Temperature
 */

// @lc code=start
class Solution
{
public:
    vector<double> convertTemperature(double celsius) {
        // 宣告內容是double類型的vector
        vector<double> res;
        // 已經知道只會放兩個元素用reserve()靜態配置, 避免多餘動態分配
        res.reserve(2);
        
        // vector可以用emplace_back, 等同於python中list的append, 省下copy
        res.emplace_back(celsius + 273.15);
        res.emplace_back(celsius * 1.80 + 32.00);
        
        return res;
    }
};
// @lc code=end

