#include <iostream>
#include <stack>
/*
172 Binary Search Tree Iterator
https://oj.leetcode.com/problems/binary-search-tree-iterator/
*/
#define MAX(a,b) (a)>(b)?(a):(b)
struct Binary_Search_Tree_Node{
    int rank;
    struct Binary_Search_Tree_Node *pl;
    struct Binary_Search_Tree_Node *pr;
};
typedef struct Binary_Search_Tree_Node node;

node* emptyNode(){
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
void destroyInOrder(node* n) {
	if(n != 0){
		destroyInOrder(n->pl);
		destroyInOrder(n->pr);
        free(n);
	}
}
void inorder(node* n) {
	if(n != 0) {
		inorder(n->pl);
		printf("%d ", n->rank);
		inorder(n->pr);
	}
}
// Get height, helper func for levelorderRec
int getHeight(node* n){
    if(n == 0){return 0;}
    return MAX(getHeight(n->pl),getHeight(n->pr))+1;
}
void levelorderRec(node* n, int level){
    if(n == 0 || level < 1){return;}
    if(level == 1){printf("%d ",n->rank);}
    levelorderRec(n->pl,level-1);
    levelorderRec(n->pr,level-1);
}
// 102
void levelorder(node* n){
    int height = getHeight(n);
    int i;
    for(i=1;i<=height;i++){
        levelorderRec(n,i);
        printf("\n");
    }
    printf("\n");
}
/*
The input is the root node, i.e.,
only available to iterate right-side nodes
*/
class BinaryTreeIterator{
public:
    BinaryTreeIterator(node* root)
    {
        m_root = root;
        m_next.push(m_root);
    }
	~BinaryTreeIterator(){}

    node* next()
    {
        node *last;
        if(m_next.empty()) return 0;

		pushNext();
        last = m_next.top();
        m_next.pop();
        return last;
    }
    
    bool hasNext()
    {
        return !m_next.empty();
    }
  
private:

    void pushNext()
    {
        node *curr, *last;
        if(m_next.empty()) return;
        
        last = m_next.top();
        m_next.pop();
        curr = last->pr;
        if(curr != 0){
            m_next.push(curr);
            curr = curr->pl;
            while(curr != 0)
            {
                m_next.push(curr);
                curr = curr->pl;
            }
        }
        m_next.push(last);
    }
    
    node* m_root;
    
    // "m_next" collects nodes after root
    // use O(height) memory
    std::stack<node*> m_next;
};

// tester
int main(int argc, char** argv){
#define NUM 31
    int arr[NUM];
    int i;
	BinaryTreeIterator* helper;

    node* n = emptyNode();
    for(i=0;i<NUM;i++){
        arr[i] = i;
    }
    initInOrder(n,arr,0,NUM-1);
    //inorder(n);putchar('\n');
    levelorder(n);putchar('\n');
    
	inorder(n->pr);putchar('\n');
    helper = new BinaryTreeIterator(n);
	while(helper->hasNext())
	{
		printf("%d ",helper->next()->rank);
	}
	putchar('\n');

	delete helper;
    destroyInOrder(n);
    return 0;
}