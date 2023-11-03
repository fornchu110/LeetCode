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
    //�פ����, ��root�Dnode��
    if(root==NULL) {
        return;
    }
    //resSize�O����, ���ȭn��*
    //�n��*resSize�A��,���M++�|�[��resSize�]�N�ܦ��O�����m+1
    //preorder:��->��->�k
    res[(*resSize)++] = root->val;
    preorder(root->left, res, resSize);
    preorder(root->right, res, resSize);    

}

int* preorderTraversal(struct TreeNode* root, int* returnSize){
    //�ʺA���t�^�ǥΪ�res�}�C
    int* res = (int*)malloc(100*sizeof(int));
    //returnSize�O����, ��*��l��*returnSize���ȷ�@��Jres��index
    *returnSize = 0;
    //�qroot�}�l��Ҧ�node�����j��preorder
    preorder(root, res, returnSize);
    //�������j�����o��e�ǰl�ܧ������G, return res
    return res;
}

// @lc code=end

