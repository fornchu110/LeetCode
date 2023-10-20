/*
 * @lc app=leetcode id=136 lang=c
 *
 * [136] Single Number
 */

// @lc code=start

//By bitwise XOR(^)
//�]���D�ػ�nums�����������F�ߤ@�����u�X�{"2��"
//�ҥH�Q��x XOR x = 0�H��0 XOR x = x���ʽ�, ��Ҧ�������XOR�Y�O����
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

