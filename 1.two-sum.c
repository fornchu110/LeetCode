/*
 * @lc app=leetcode id=1 lang=c
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// BY hash table
struct hashTable {
    int key;
    int val;
    UT_hash_handle hh;
};

struct hashTable* hashtable;

struct hashTable* find(int ikey) {
    struct hashTable* tmp;
    HASH_FIND_INT(hashtable, &ikey, tmp);
    return tmp;
}

void insert(int ikey, int ival) {
    struct hashTable* it = find(ikey);
    if (it == NULL) {
        struct hashTable *tmp = malloc(sizeof(struct hashTable));
        tmp->key = ikey;
        tmp->val = ival;
        HASH_ADD_INT(hashtable, key, tmp);
    }
    else {
        it->val = ival;
    }
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    hashtable = NULL;
    for (int i = 0; i < numsSize; i++) {
        struct hashTable* it = find(target - nums[i]);
        if (it != NULL) {
            int* ret = malloc(sizeof(int) * 2);
            ret[0] = it->val, ret[1] = i;
            *returnSize = 2;
            return ret;
        }
        insert(nums[i], i);
    }
    *returnSize = 0;
    return NULL;
}

// By for loop
// int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
//     int i, j;
//     for(i=0;i<numsSize-1;i++) {
//         for(j=i+1;j<numsSize;j++) {
//             if(target-nums[i]==nums[j]) {
//                 int* ret = (int*)malloc(2*sizeof(int));
//                 ret[0] = i;
//                 ret[1] = j;
//                 *returnSize = 2;
//                 return ret;
//             }
//         }
//     }
//     *returnSize = 0;
//     return 0;
// }
// @lc code=end

