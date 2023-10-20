/*
 * @lc app=leetcode id=136 lang=c
 *
 * [136] Single Number
 */

// @lc code=start

//By bitwise XOR(^)
//因為題目說nums內的元素除了唯一的都只出現"2次"
//所以利用x XOR x = 0以及0 XOR x = x的性質, 把所有元素做XOR即是答案
int singleNumber(int* nums, int numsSize){
    int i, ret = 0;
    for(i=0;i<numsSize;i++){
        ret^=nums[i];
    }
    return ret;
}

//By hashtable
// struct hashTable {
//     int key;
//     int val;
//     UT_hash_handle hh;
// };
// struct hashTable* hashtable;

// struct hashTable* find(int key) {
//     struct hashTable* tmp;
//     HASH_FIND_INT(hashtable, &key, tmp);
//     return tmp;
// }

// void insert(int key, int val) {
//     struct hashTable* it = find(key);
//     if(it==NULL) {
//         struct hashTable* tmp = (struct hashTable*)malloc(sizeof(struct hashTable));
//         tmp->key = key;
//         tmp->val = val;
//         HASH_ADD_INT(hashtable, key, tmp);
//     }
//     else {
//         it->val++;
//     }
// }

// int singleNumber(int* nums, int numsSize){
//     hashtable = NULL;
//     int i, j;
//     for(i=0;i<numsSize;i++) {
//         insert(nums[i], 1);
//     }
//     for(i=0;i<numsSize;i++) {
//         struct hashTable* tmp = find(nums[i]);
//         if(tmp->val==1) {
//             return tmp->key;
//         }
//     }
//     return 0;
// }

// @lc code=end

