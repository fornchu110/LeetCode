/*
 * @lc app=leetcode id=144 lang=c
 *
 * [144] Binary Tree Preorder Traversal
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

// By recursive
void preorder(struct TreeNode* root, int* res, int* resSize) {
    //終止條件, 當root非node時
    if(root==NULL) {
        return;
    }
    //resSize是指標, 取值要用*
    //要對*resSize括號,不然++會加到resSize也就變成記憶體位置+1
    //preorder:中->左->右
    res[(*resSize)++] = root->val;
    preorder(root->left, res, resSize);
    preorder(root->right, res, resSize);    

}

int* preorderTraversal(struct TreeNode* root, int* returnSize){
    //動態分配回傳用的res陣列
    int* res = (int*)malloc(100*sizeof(int));
    //returnSize是指標, 用*初始化*returnSize的值當作放入res的index
    *returnSize = 0;
    //從root開始對所有node做遞迴的preorder
    preorder(root, res, returnSize);
    //全部遞迴完成得到前序追蹤完的結果, return res
    return res;
}

// @lc code=end
