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
    int val;
    Node* from;
    Node* next;

    void operator = (int val)
    {
        this->val = val;
    }
};

class LRUCache
{
private:

    Node* head; // head node is reserved
    Node* tail;
    std::unordered_map<int,Node*> m_map; // key:pos
    int capacity;
 
public:
    LRUCache(int capacity)
    {
        if(capacity < 1)
        {
            printf("LRU Cache's capacity cannot be less than 1, reset to 1\n");
            this->capacity = 1;
        }
        else 
            this->capacity = capacity;

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

    inline size_t getCapacity(void)
    {
        return this->capacity;
    }

    void print(void)
    {
        Node* p = head->next;
        int i =0;
        while(p){
            std::cout<<i++<<" : ("<<p->key<<" "<<(char)p->val<<")\n";
            p = p->next;
        }
        printf("\n");
        p = 0;
    }

    // move current node in list to list end
    void move2End(Node* pos)
    {
        if(pos != tail)
        {
            pos->from->next = pos->next;
            pos->next->from = pos->from;
            pushBack(pos);
        }
    }

    // push a node to back
    void pushBack(Node* pos)
    {
        pos->from = tail;
        pos->next = 0;
        tail->next = pos;
        tail = pos;
    }

    // getter
    int get(int key)
    {
        Node* pos = 0;
        int val;
        auto it = m_map.find(key);

        if(it == m_map.end())
        {
            //std::cout<<"Not found\n";
            return -1;
        }

        pos = it->second;
        val = pos->val;
        move2End(pos);
        return val;
    }

    // setter
    void set(int key, int val)
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

int main(int argc, char* argv[])
{
    LRUCache* p = new LRUCache(3);
    std::cout<<"capacity: "<<p->getCapacity()<<"\n";
    
    p->set(5,'A');
    p->set(10,'B'); p->print();
    p->set(15,'C'); p->print();
    p->set(5,'M');  p->print();
    p->set(20,'X'); p->print();

    delete p;
    return 0;
}
