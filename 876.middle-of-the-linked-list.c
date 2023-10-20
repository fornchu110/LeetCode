/*
 * @lc app=leetcode id=876 lang=c
 *
 * [876] Middle of the Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// By one pointer, time: O(n), space: O(1)
// 記住用新指標都要先malloc出來
struct ListNode* middleNode(struct ListNode* head){
    int n = 0;
    if(head==NULL) {
        return head;
    }
    struct ListNode *dummy = malloc(sizeof(struct ListNode));
    struct ListNode *cur = malloc(sizeof(struct ListNode));
    dummy->next = head;
    cur = dummy;
    while(cur->next!=NULL) {
        n++;
        cur = cur->next;
    }
    n /= 2;
    cur = dummy->next;
    while(n--) {
        cur = cur->next;
    }
    return cur;
}

// By fast-slow pointer, time: O(n), space: O(1) 
// struct ListNode* middleNode(struct ListNode* head){
//     struct ListNode *dummy = malloc(sizeof(struct ListNode));
//     struct ListNode *fast = malloc(sizeof(struct ListNode));
//     struct ListNode *slow = malloc(sizeof(struct ListNode));
//     dummy->next = head;
//     fast = head;
//     slow = head;
//     while(fast!=NULL&&fast->next!=NULL) {
//         slow = slow->next;
//         fast = fast->next->next;
//     }
//     return slow;
// }

// @lc code=end

