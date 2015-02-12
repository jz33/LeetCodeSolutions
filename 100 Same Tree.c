/*
100 Same Tree
https://oj.leetcode.com/problems/same-tree/
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
void isSameTree(node* x, node* y, int* flag){
    if(*flag == 1){
        if(x == 0 && y ==0) return;
        if((x != 0 && y ==0) || (x== 0 && y !=0)){
            *flag = 0;
            return;
        }
        if(x->rank == y->rank){
            isSameTree(x->pl,y->pl,flag);
            if(*flag == 1) isSameTree(x->pr,y->pr,flag);
        } else {
            *flag = 0;
        }
    }
}
int main(int argc, char** argv){
    //TODO: test
    return 0;
}