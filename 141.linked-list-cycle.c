/*
 * @lc app=leetcode id=141 lang=c
 *
 * [141] Linked List Cycle
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// By fast-slow pointer, time: O(n), space: O(1)
bool hasCycle(struct ListNode *head) {
    // head是指標所以都用->操作node
    if(head==NULL||head->next==NULL) {
        return false;
    }
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    while(fast!=NULL&&fast->next!=NULL) {
        fast = fast->next->next;
        slow = slow->next;
        if(fast==slow) {
            return true;
        }
    }
    return false;
}

// @lc code=end

