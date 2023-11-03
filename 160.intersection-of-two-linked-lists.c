<<<<<<< HEAD
/*
 * @lc app=leetcode id=160 lang=c
 *
 * [160] Intersection of Two Linked Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if(headA==NULL||headB==NULL) {
        return NULL;
    }
    struct ListNode *A = headA;
    struct ListNode *B = headB;
    while(A!=B) {
        if(A!=NULL) {
            A = A->next;
        }
        else {
            A = headB;
        }
        if(B!=NULL) {
            B = B->next;
        }
        else {
            B = headA;
        }
    }
    return A;
}

// @lc code=end

=======
/*
 * @lc app=leetcode id=160 lang=c
 *
 * [160] Intersection of Two Linked Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if(headA==NULL||headB==NULL) {
        return NULL;
    }
    struct ListNode *A = headA;
    struct ListNode *B = headB;
    while(A!=B) {
        if(A!=NULL) {
            A = A->next;
        }
        else {
            A = headB;
        }
        if(B!=NULL) {
            B = B->next;
        }
        else {
            B = headA;
        }
    }
    return A;
}

// @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
