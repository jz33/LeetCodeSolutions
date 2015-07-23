#include <stack>
#include <vector>
#include <stdlib.h>

#define MAX(a,b) (a)>(b)?(a):(b)
struct Binary_Search_Tree_Node{
    int rank;
    struct Binary_Search_Tree_Node *pl;
    struct Binary_Search_Tree_Node *pr;
};
typedef struct Binary_Search_Tree_Node node;

node* emptyNode()
{
    node* n = (node*)malloc(sizeof(node));
    n->rank = -1;
    n->pl = 0;
    n->pr = 0;
    return n;
}
void initInOrder(node* n, int* arr, int start, int end){
    int mid = (start+end)>>1;
    n->rank = arr[mid];
    
    if(start <= mid-1) {
    	n->pl = emptyNode();
    	initInOrder(n->pl, arr, start, mid-1);
    }
    if(mid+1 <= end) {
    	n->pr = emptyNode();
    	initInOrder(n->pr, arr, mid+1, end);
    }
}
void destroyInOrder(node* n)
{
    if(n != 0){
    	destroyInOrder(n->pl);
    	destroyInOrder(n->pr);
        free(n);
    }
}
void postorder(node* n)
{
    if(n != 0)
    {
    	postorder(n->pl);
    	postorder(n->pr);
    	printf("%d ", n->rank);
    }
}
std::vector<int> preorderTraversal(node* root)
{
    std::vector<int> ret;
    if(root == 0)  return ret;
    
    std::stack<node*> st;
    st.push(root);
    
    node *prev = root;
    node *next = root;
    
    while(!st.empty())
    {
        next = st.top();
        
        /*
        $next is above $prev or $next is leaf
        */
        if(
            (next->pl == 0 && next->pr == 0) ||
            next->pl == prev ||
            next->pr == prev
          )
        {
            printf("%d ", next->rank);
            ret.push_back(next->rank);
            st.pop();
        }
        else
        {
            if(next->pr != 0) st.push(next->pr);
            if(next->pl != 0) st.push(next->pl); 
        }
        prev = next;
    }
    return ret;
}

int main()
{
#define NUM 2
    int arr[NUM];
    int i;
    node* n = emptyNode();
    for(i=0;i<NUM;i++){
        arr[i] = i;
    }
    initInOrder(n,arr,0,NUM-1);
    
    postorder(n);putchar('\n');
    preorderTraversal(n);putchar('\n');
    
    destroyInOrder(n);
    return 0;
}
