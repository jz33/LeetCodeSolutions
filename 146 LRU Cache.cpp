#include <iostream>
#include <string>
#include <unordered_map>
/*
146 LRU Cache
https://oj.leetcode.com/problems/lru-cache/
http://yucoding.blogspot.ca/2013/12/leetcode-question-lru-cache.html
*/
// a double linked list node
class Node{
public:
    int key;
    std::string val;
    Node* from;
    Node* next;

    void operator=(std::string val){
        this->val = val;
    }
};

class LRUCache
{
private:

    Node* head; // head node is reserved
    Node* tail;
    std::unordered_map<int,Node*> m_map; // key:pos
    size_t capacity;
 
public:
    LRUCache(size_t capacity)
    {
        if(capacity == 0)
        {
            printf("LRU Cache's capacity cannot be 0, reset to 1\n");
            capacity = 1;
        }
        else this->capacity = capacity;

        head = new Node();
        tail = head;
    }
    
    virtual ~LRUCache(){
        Node* p = 0;
        while(head != tail){
            p = head;
            head = head->next;
            delete p;
        }
        delete tail;
        head = 0;
        tail = 0;
        p = 0;
    }

    inline size_t getCapacity(void){return this->capacity;}

    // print all
    void print(void)
    {
        printf("LRU current object address: %p\n",this);
        Node* p = head->next;
        size_t i =0;
        while(p){
            printf("%u : (%d %s)\n",i++,p->key, p->val.c_str());
            p = p->next;
        }
        printf("\n");
        p = 0;
    }

    // move current node in list to list end
    void move2End(Node* &pos){
        if(pos != tail){
            pos->from->next = pos->next;
            pos->next->from = pos->from;
            pushBack(pos);
        }
    }

    // push a node to back
    void pushBack(Node* &in){
        in->from = tail;
        in->next = 0;
        tail->next = in;
        tail = in;
    }

    // getter
    std::string get(int key)
    {
        Node* pos = 0;
        std::string val;
        auto it = m_map.find(key);

        if(it == m_map.end()) return "";

        pos = it->second;
        val = pos->val;
        move2End(pos);
        return val;
    }

    // operator, get ref
    Node*& operator[](const int& key)
    {
        Node* pos = 0;
        auto it = m_map.find(key);
    
        if(it == m_map.end())
        {
            // replace lru node
            if(m_map.size() == this->capacity)
            {
                pos = head->next;
                m_map.erase(pos->key);
                move2End(pos);
            }
            // push_back
            else
            {   
                pos = new Node();
                pushBack(pos);
            }
            pos->key = key;         
        }
        // set
        else
        {
            pos = it->second;
            move2End(pos);
        }
        m_map[key] = pos;
        return tail;
    }

    // setter
    void set(int key, const std::string val)
    {
        Node* pos = 0;
        auto it = m_map.find(key);
    
        if(it == m_map.end())
        {
            // replace lru node
            if(m_map.size() == this->capacity)
            {
                pos = head->next;
                m_map.erase(pos->key);
                move2End(pos);
            }
            // push_back
            else
            {   
                pos = new Node();
                pushBack(pos);
            }
            pos->key = key;
            pos->val = val;            
        }
        // set
        else
        {
            pos = it->second;
            pos->val = val;
            move2End(pos);
        }
        m_map[key] = pos;
    }
};
void someops(LRUCache& p)
{
    p.set(5,"A");
    p.set(10,"B"); p.print();
    p.set(15,"C"); p.print();
    p.set(5,"M");  p.print();
    p.set(20,"X"); p.print();

    p.set(5,"A");std::cout<<p[5]->val<<"\n";

    p[20]->val = "NEW";p.print();
    *p[20] = "def";p.print();
}
int main(int argc, char* argv[])
{
    LRUCache* p = new LRUCache(3);
    printf("capacity: %u\n",p->getCapacity());
    p->set(5,"A");
    p->set(10,"B"); p->print();
    p->set(15,"C"); p->print();
    p->set(5,"M");  p->print();
    p->set(20,"X"); p->print();
    delete p;

    LRUCache x(3);
    someops(x);

    return 0;
}
