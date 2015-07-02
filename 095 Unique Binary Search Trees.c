/*
95 Unique Binary Search Trees
https://oj.leetcode.com/problems/unique-binary-search-trees/
*/
/*
Catalan number:
(2*N)! / (n+1)!*n!
*/
int Catalan(int n){
    return n==1 ? 1 : (int)((long long)Catalan(n-1)*(4 * n - 2)/(n + 1));
}

int numTrees(int n) {
    return Catalan(n);
}

int main(){
    return 0; 
}
