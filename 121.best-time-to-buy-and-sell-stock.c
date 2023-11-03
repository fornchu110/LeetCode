<<<<<<< HEAD
/*
 * @lc app=leetcode id=121 lang=c
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
int maxProfit(int* prices, int pricesSize){
    int i;
    int min = 1e+9;
    int maxProfit = 0;
    for(i=0;i<pricesSize;i++) {
        if(prices[i]-min>maxProfit) {
            maxProfit = prices[i]-min;
        }
        if(prices[i]<min) {
            min = prices[i];
        }
    }
    return maxProfit;
}

// @lc code=end

=======
/*
 * @lc app=leetcode id=121 lang=c
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
int maxProfit(int* prices, int pricesSize){
    int i;
    int min = 1e+9;
    int maxProfit = 0;
    for(i=0;i<pricesSize;i++) {
        if(prices[i]-min>maxProfit) {
            maxProfit = prices[i]-min;
        }
        if(prices[i]<min) {
            min = prices[i];
        }
    }
    return maxProfit;
}

// @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
