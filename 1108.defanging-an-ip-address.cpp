/*
 * @lc app=leetcode id=1108 lang=cpp
 *
 * [1108] Defanging an IP Address
 */

// @lc code=start
class Solution 
{
public:
    string defangIPaddr(string address)
    {
        string res;
        // 避免沒必要的動態分配
        res.reserve(address.size());
        // 記得用const auto&來迭代, 避免修改和不必要的value copy
        for(const auto& c : address)
        {
            if(c=='.')
            {
                res += "[.]";
            }
            else
            {
                res += c;
            }
        }
        return res;
    }
};
// @lc code=end

