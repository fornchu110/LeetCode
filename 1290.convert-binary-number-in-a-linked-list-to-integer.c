/*
 * @lc app=leetcode id=1290 lang=c
 *
 * [1290] Convert Binary Number in a Linked List to Integer
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// By simulation and bitwise, time: O(n), space: O(1)
// ¦hµ½¥Îbitwise¾Þ§@
int getDecimalValue(struct ListNode* head){
    struct ListNode* cur = malloc(sizeof(struct ListNode));
    cur = head;
    int res = 0;
    while(cur!=NULL) {
        res = (res<<1)|cur->val;
        cur = cur->next;
    }
    return res;
}

// @lc code=end

