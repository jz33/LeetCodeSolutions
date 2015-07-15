#include <iostream>
#include <sstream>
#include <unordered_map>
using namespace std;
/*
Implement Trie
https://leetcode.com/problems/implement-trie-prefix-tree/

Using hash_map to hold children for general purpose
For this question, the container can be constant array
*/
class TrieNode
{
public:

    char key = ' ';
    bool ended = false; // if there is a word ends here
    unordered_map<char,TrieNode*> sub;
    
    TrieNode(){}
    
    TrieNode(char key)
    {
        this->key = key;
    }
    
    ~TrieNode()
    {
        for(auto i = sub.begin();i != sub.end();i++)
        {
            delete i->second;
        }
    }
    
    void insert(string& word, size_t offset)
    {
        char c;
        if(offset == word.size())
        {
            ended = true;
        }
        else if(offset < word.size())
        {
            c = word[offset];
            if(sub.find(c) == sub.end())
            {
                sub[c] = new TrieNode(c);
            }
            sub[c]->insert(word,offset+1);
        }
    }
    
    /*
    If $word is of one whole word in trie
    */
    bool search(string& word, size_t offset)
    {
        char c;
        if(offset == word.size())
        {
            return ended;
        }
        else if(offset < word.size())
        {
            c = word[offset];
            if(sub.find(c) != sub.end())
            {
                return sub[c]->search(word,offset+1);
            }
        }
        return false;
    }
    
    /*
    If $word is of prefix of any words in trie
    */
    bool prefix(string& word,size_t offset)
    {
        char c;
        if(offset == word.size())
        {
            return true;
        }
        else if(offset < word.size())
        {
            c = word[offset];
            if(sub.find(c) != sub.end())
            {
                return sub[c]->prefix(word,offset+1);
            }
        }
        return false;
    }
};

class Trie
{
public:

    Trie()
    {
        root = new TrieNode(' ');
    }
    
    ~Trie()
    {
        delete root;
    }

    // Inserts a word into the trie.
    void insert(string word)
    {
        root->insert(word,0);
    }

    // Returns if the word is in the trie.
    bool search(string word)
    {
        return root->search(word,0);
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string word)
    {
        return root->prefix(word,0);
    }

private:
    TrieNode* root;
};

int main()
{
    Trie* t = new Trie();
    
    t->insert("a");
    t->insert("abc");
    
    cout<<t->search("a")<<"\n";
    cout<<t->search("ab")<<"\n";
    cout<<t->search("abc")<<"\n";
    
    cout<<t->startsWith("a")<<"\n";
    cout<<t->startsWith("ab")<<"\n";
    cout<<t->startsWith("abc")<<"\n";
    
    delete t;
    return 0;
}
