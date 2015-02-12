/*
10 Symmetric Tree
https://oj.leetcode.com/problems/symmetric-tree/
*/
struct Binary_Search_Tree_Node{
    int rank;
    struct Binary_Search_Tree_Node *pl;
    struct Binary_Search_Tree_Node *pr;
};
typedef struct Binary_Search_Tree_Node node;
/*
"flag" is init as 1
*/
void isSymmetricTreeRec(node* x, node* y, int* flag){
    if(*flag == 1){
        if(x == 0 && y == 0) return;
        if((x != 0 && y ==0) || (x== 0 && y !=0)){
            *flag = 0;
            return;
        }
        if(x->rank == y->rank){
            isSymmetricTreeRec(x->pr,y->pl,flag);
            if(*flag == 1) isSymmetricTreeRec(x->pl,y->pr,flag);
        } else {
            *flag = 0;
        }
    }
}
int isSymmetricTree(node* x){
    int flag;
    if(x==0) return 1;
    
    flag = 1;
    isSymmetricTreeRec(x->pl,x->pr,&flag);
}
int main(int argc, char** argv){
    //TODO: test
    return 0;
}