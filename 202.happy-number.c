<<<<<<< HEAD
/*
 * @lc app=leetcode id=202 lang=c
 *
 * [202] Happy Number
 */

// @lc code=start

//By array��hash table, �]�u�ݭn��key����value
bool isHappy(int n){
    int hash[5000];
    memset(hash, 0 ,sizeof(hash));
    while(true){
        int res = 0;
        while(n){
            int a = (n % 10);
            res += a * a;
            n /= 10;
        }
        if(res == 1) return true;
        hash[res]++;//�C���ores�N��hash[res]+1�N���L�o��res�F
        if(hash[res] > 1) return false;//�u�nhash[res]�W�L1�N����,�i�J�L�a�j��
        n = res;
    }
}

//By ���Whashtable
// struct hashTable {
//     int key;
//     UT_hash_handle hh;
// };
// struct hashTable* hashtable;

// struct hashTable* find(key) {
//     struct hashTable* tmp;
//     HASH_FIND_INT(hashtable, &key, tmp);
//     return tmp;
// }

// void insert(key) {
//     struct hashTable* it = find(key);
//     if(it==NULL) {
//         struct hashTable* tmp = (struct hashTable*)malloc(sizeof(struct hashTable));
//         tmp->key = key;
//         HASH_ADD_INT(hashtable, key, tmp);
//     }
//     else {
//         return false;
//     }
// }

// bool isHappy(int n){
//     int a, res, ret = 0;
//     while(1) {
//         res = 0;
//         while(n) {
//             a = n%10;
//             res += a*a;
//             n/=10;
//         }
//         if(res==1) {
//             return true;
//         }
//         insert(res);
//         n = res;
//     }
//     return NULL;
// }

// @lc code=end

=======
/*
 * @lc app=leetcode id=202 lang=c
 *
 * [202] Happy Number
 */

// @lc code=start

//By array��hash table, �]�u�ݭn��key����value
bool isHappy(int n){
    int hash[5000];
    memset(hash, 0 ,sizeof(hash));
    while(true){
        int res = 0;
        while(n){
            int a = (n % 10);
            res += a * a;
            n /= 10;
        }
        if(res == 1) return true;
        hash[res]++;//�C���ores�N��hash[res]+1�N���L�o��res�F
        if(hash[res] > 1) return false;//�u�nhash[res]�W�L1�N����,�i�J�L�a�j��
        n = res;
    }
}

//By ���Whashtable
// struct hashTable {
//     int key;
//     UT_hash_handle hh;
// };
// struct hashTable* hashtable;

// struct hashTable* find(key) {
//     struct hashTable* tmp;
//     HASH_FIND_INT(hashtable, &key, tmp);
//     return tmp;
// }

// void insert(key) {
//     struct hashTable* it = find(key);
//     if(it==NULL) {
//         struct hashTable* tmp = (struct hashTable*)malloc(sizeof(struct hashTable));
//         tmp->key = key;
//         HASH_ADD_INT(hashtable, key, tmp);
//     }
//     else {
//         return false;
//     }
// }

// bool isHappy(int n){
//     int a, res, ret = 0;
//     while(1) {
//         res = 0;
//         while(n) {
//             a = n%10;
//             res += a*a;
//             n/=10;
//         }
//         if(res==1) {
//             return true;
//         }
//         insert(res);
//         n = res;
//     }
//     return NULL;
// }

// @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
