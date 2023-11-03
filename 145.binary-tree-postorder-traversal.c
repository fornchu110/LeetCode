/*
 * @lc app=leetcode id=145 lang=c
 *
 * [145] Binary Tree Postorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

//By recursive
void postorder(struct TreeNode*root, int* res, int* resSize) {
    //終止條件, 當非node時不用遞迴
    if(root==NULL) {
        return;
    }
    //後序追蹤:左->右->中
    postorder(root->left, res, resSize);
    postorder(root->right, res, resSize);
    //resSize是指標, *resSize才是index
    //將中的val放入res[*resSize], 並且將*resSize++
    res[(*resSize)++] = root->val;
    return;
}

int* postorderTraversal(struct TreeNode* root, int* returnSize){
    //動態宣告回傳後序追蹤結果的res陣列
    int* res = (int*)malloc(100*sizeof(int));
    //returnSize是指標, 初始化*resturnSize作為將node放入res之index
    *returnSize = 0;
    //從root開始對所有node遞迴做後序追蹤
    postorder(root, res, returnSize);
    //完成所有遞迴, 回傳結果
    return res;
}
// @lc code=end

