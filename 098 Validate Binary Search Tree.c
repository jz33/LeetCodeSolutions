/*
98 Validate Binary Search Tree
https://oj.leetcode.com/problems/validate-binary-search-tree/
*/
struct Binary_Search_Tree_Node{
    int rank;
    struct Binary_Search_Tree_Node *pl;
    struct Binary_Search_Tree_Node *pr;
};
typedef struct Binary_Search_Tree_Node node;

/*
A normal way based on in order traversal
"flag" is result, init as 1
"prev" is value or previous node of the in order traversal
"prev" is init as INT_MIN
*/
void isValidBST(node* head, int* prev, int* flag){
    if(*flag == 1 && head != 0){
        isValidBST(head->pl,prev,flag);
        if(prev > head->rank){
            *flag = 0;
            return;
        } else {
            *prev = head->rank;
        }
        isValidBST(head->pr,prev,flag);
    }
}
/*
Another way
"flag" is result, init as 1
"minRank" is init as INT_MIN
"maxRank" is init as INT_MAX
*/
void minMax(node* head, int minRank, int maxRank, int* flag){
    if(*flag == 1 && head != 0){
        if(head->rank < minRank || head->rank > maxRank){
            *flag = 0;
            return;
        } else {
            minMax(head->pl, minRank, head->rank, flag);
            if(*flag == 1)
                minMax(head->pr, head->rank, maxRank, flag);
        }
    }
}
int main(int argc, char** argv){
    //TODO: test
    return 0;
}