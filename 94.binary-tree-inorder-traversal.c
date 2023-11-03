/*
 * @lc app=leetcode id=94 lang=c
 *
 * [94] Binary Tree Inorder Traversal
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
// resSize是為了知道當下放入之node該放在res的哪個index
void inorder(struct TreeNode* root, int* res, int* resSize) {
    //終止條件, 非node時沒辦法遞迴, 直接return
    if (!root) {
        return;
    }
    //inoder順序是:左->中->右, 中不會有子樹
    //左子樹做遞迴
    inorder(root->left, res, resSize);
    //左子樹遞迴做完, 將root放入並把reSize+1(等同下個root要放入的位置)
    res[(*resSize)++] = root->val;
    //左子樹和root都做完才做右子樹
    inorder(root->right, res, resSize);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    //對tree所有node做遞迴, 每次都以當下的node為root
    int* res = malloc(sizeof(int)*100);
    //一開始一定是從res[0]開始放入node, 所以returnSize = 0
    *returnSize = 0;
    inorder(root, res, returnSize);
    //等完成對所有node的inorder追蹤後, resSize便是returnSize=node總數
    return res;
}

// @lc code=end

