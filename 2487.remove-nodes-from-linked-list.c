/*
 * @lc app=leetcode id=2487 lang=c
 *
 * [2487] Remove Nodes From Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// By iterative, time: O(n), space: O(n)
struct ListNode* reverseList (struct ListNode *head) {
    struct ListNode *prev = NULL, *cur = head, *next;
    while(cur!=NULL) {
        next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }
    return prev;
}

struct ListNode* removeNodes(struct ListNode* head) {
    head = reverseList(head);
    struct ListNode *cur = head;
    while(cur->next!=NULL) {
        if(cur->next->val<cur->val) {
            cur->next = cur->next->next;
        }
        else {
            cur = cur->next;
        }
    }
    return reverseList(head);
}

// // By recursive, time: O(n), space: O(n)
// struct ListNode* removeNodes(struct ListNode* head) {
//     if(head->next==NULL) {
//         return head;
//     }
//     struct ListNode *com = removeNodes(head->next);
//     if(com->val>head->val) {
//         return com;
//     }
//     head->next = com;
//     return head;
// }

// @lc code=end

