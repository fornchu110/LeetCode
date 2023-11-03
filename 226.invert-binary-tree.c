/*
 * @lc app=leetcode id=226 lang=c
 *
 * [226] Invert Binary Tree
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
struct TreeNode* invertTree(struct TreeNode* root){
    //root���V�F�ثe�Ҧb��node, �O����
    //�פ����,��S������Dnode�ɰ���
    if(root==NULL) {
        return NULL;
    }
    //�`�N�n�洫���O���node�����c, ���O�u��value
    //�إ߫��V���l�I�M�k�l�I������
    struct TreeNode* left = invertTree(root->left);
    struct TreeNode* right = invertTree(root->right);
    //���k�l�I�洫
    root->left = right;
    root->right = left;
    //�^�ǥ洫�����k�l�I��node
    //�]�N�O���q�̫�@�h�l�I�N�洫����node�^�ǵ���parent����u����root�ɵ���
    return root;
}

// @lc code=end

