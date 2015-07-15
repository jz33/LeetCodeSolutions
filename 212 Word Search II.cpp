#include <iostream>
#include <sstream>
#include <vector>
using namespace std;
/*
Word Search II
https://leetcode.com/problems/word-search-ii/
*/
#define VISITED '!'
#define SIZE 26

typedef std::vector<std::vector<char> > MAT;
typedef std::vector<std::string> VEC;

VEC pool;
size_t ROW;
size_t COL;

class TrieNode
{
public:

    char key = ' ';
    bool ended = false; // if there is a word ends here
    TrieNode* sub[SIZE];
    
    TrieNode(char key)
    {
        this->key = key;
        for(size_t i = 0;i != SIZE;i++)
            this->sub[i] = 0;
    }
    
    ~TrieNode()
    {
        for(size_t i = 0;i != SIZE;i++)
        {
            delete sub[i];
        }
    }
    
    void insert(string& word, size_t offset)
    {
        char c;
        int k;
        if(offset == word.size())
        {
            ended = true;
        }
        else if(offset < word.size())
        {
            c = word[offset];
            k = c - 'a';
            if(sub[k] == 0)
            {
                sub[k] = new TrieNode(c);
            }
            sub[k]->insert(word,offset+1);
        }
    }
};

void recursive(MAT& mat, TrieNode* node, std::string buf, size_t row, size_t col)
{
    char ori;
    int k;
    if(node == 0 || mat[row][col] == VISITED)
        return; 

    ori = mat[row][col];
    k = ori-'a';
    if(node->sub[k] != 0)
    {
        buf += ori;
    }
    else
        return;
    
    if(node->sub[k]->ended)
    {
        node->sub[k]->ended = false;
        pool.push_back(buf);
    }
    
    mat[row][col] = VISITED; 
    
    if(row > 0) 
        recursive(mat,node->sub[k], buf,row - 1, col);
    if(row < ROW - 1) 
        recursive(mat,node->sub[k], buf,row + 1, col);
    if(col > 0)
        recursive(mat,node->sub[k], buf,row, col - 1);
    if(col < COL - 1) 
        recursive(mat,node->sub[k], buf,row, col + 1);

    mat[row][col] = ori;
}

// api
VEC findWords(MAT& board, VEC& words)
{
    pool.clear();
    ROW = board.size();
    if(ROW == 0) return pool;
    COL = board[0].size();
    if(COL == 0) return pool;
    
    TrieNode* node = new TrieNode(' ');
    for(auto i = words.begin();i!=words.end();i++)
    {
        node->insert(*i,0);
    }
    
    for(size_t i = 0;i<ROW;i++)
    {
        for(size_t j = 0;j<COL;j++)
        {
            std::string buf = "";
            recursive(board,node,buf,i,j);          
        }
    }
    delete node;
    return pool;
}

int main()
{
    char arr[] = {\
        'o','a','a','n',\
        'e','t','a','e',\
        'i','h','k','r',\
        'i','f','l','v' \
    };
    MAT board;
    
    for(size_t i = 0;i<16;i += 4)
    {
        std::vector<char> one(arr+i,arr+i+4);
        board.push_back(one);
    }
    
    VEC words;
    words.push_back("oath");
    words.push_back("pea");
    words.push_back("eat");
    words.push_back("rain");
    
    findWords(board,words);

    return 0;
}
