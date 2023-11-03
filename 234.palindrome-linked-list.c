/*
 * @lc app=leetcode id=234 lang=c
 *
 * [234] Palindrome Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// By double pointer, time: O(n), space: O(n)
bool isPalindrome(struct ListNode* head) {
    int palin[100000], idx = 0;
    while (head!=NULL) {
        palin[idx++] = head->val;
        head = head->next;
    }
    //當頭尾指標交錯或相等就不用比較了
    for (int i=0, j=idx-1; i<j;++i,--j) {
        if (palin[i]!=palin[j]) {
            return false;
        }
    }
    return true;
}

// @lc code=end