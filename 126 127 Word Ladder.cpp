#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <stack>
#include <unordered_set>
#include <unordered_map>
/*
126 Word Ladder
127 Word Ladder II
https://oj.leetcode.com/problems/word-ladder/
https://oj.leetcode.com/problems/word-ladder-ii/

Input sample:
hit
cog
hot dot dog lot log

   hit => start
    |
   hot => entries   \
  /   \
dot    lot           tree                       
|       |
dog    log => exits /
  \   /
   cog => ended
*/
typedef char** MAT;
typedef std::vector<std::string> STRLINE;
typedef std::vector<int> INTLINE;
typedef std::unordered_map<int,INTLINE> ROW;//string index : upper level indexes
typedef std::unordered_set<int> SET;
typedef std::vector<ROW> TREE;

bool isLinked(const std::string& tag, const std::string& src){
    int diff = 0;
    auto i = tag.begin();
    auto j = src.begin();
    for(;i!=tag.end() && j!=src.end() && diff<2;i++,j++)
        if(*i!=*j) diff++;
    return diff == 1;
}
/*
init exit set
init graph
init entry row
*/
void init(const std::string& start, const std::string& ended, const STRLINE& dict,
ROW& entries, SET& exits, MAT& graph, int& N){
    N = (int)dict.size();
    graph = (char**)malloc(N*sizeof(char*));
    
    for(int i=0;i!=N;i++){
        if(isLinked(start,dict[i])){
            INTLINE vec(1,-1); // start std::string index is -1
            entries.insert(std::pair<int,INTLINE>(i,vec));
        }
        if(isLinked(ended,dict[i])) exits.insert(i);
        
        graph[i] = (char*)calloc(N,sizeof(char));
        for(int j=0;j!=N;j++){     
            if(j==i) continue;
            if(isLinked(dict[i],dict[j])) graph[i][j] = 1;
        }
    }
#if OUTPUT_FILE
	ofstream out("../out.txt");
	for(int i=0;i!=N;i++){
		for(int j=0;j!=N;j++){
			char c = graph[i][j];
			if(c==1) out<<"1 ";
			else out<<"0 ";
		}
		out<<"\n";
	}
	out.close();
#endif
}
/*
Find if a key exists in upper tree rows
*/
bool isKeyIn(TREE& tree, int& tag){
    for(auto i = tree.begin();i!=tree.end();i++){
        if(i->find(tag)!=i->end()) return true;
    }
    return false;
}
/*
*/
bool iterate(ROW& entries, SET& exits, MAT& graph, const int& N, TREE& tree){
    int solCtr = 0;
	if(entries.empty()) return 0;
    tree.push_back(entries);
    for(std::size_t level = 0;level<N-entries.size();level++){
        ROW& curr = tree[level];
        ROW next;
        for(auto i = curr.begin();i!=curr.end();i++){
            int x = i->first;
            if(exits.find(x)!= exits.end()) return 1;
            
            // find linked element of x in graph[x]
            for(auto k = 0;k<N;k++)
                if(graph[x][k]==1)
                    if(!isKeyIn(tree,k))
						next[k].push_back(i->first);           
        }
        if(next.empty()) return 0;
		tree.push_back(next);
    }
    return 0;
}
/*
*/
void outputRec(TREE& tree,
std::vector<std::stack<int> >& res, std::stack<int>& buf, int level, int node){
    auto in  = tree[level].find(node); // must found
    buf.push(in->first);
    if(level==0){
        res.push_back(buf); return;
    }
    
    INTLINE& from = in->second;
    for(auto j = from.begin();j!=from.end();j++){
        std::stack<int> newbuf(buf);
        outputRec(tree,res,newbuf,level-1,*j);
    }
}
/*
Notice exits are not necessary equal to bottom level of tree
*/
void output(const std::string& start, const std::string& ended, const STRLINE& dict,
SET& exits, TREE& tree){
    std::vector<std::stack<int> > res;
    std::size_t N = tree.size();
    for(auto i = exits.begin();i!=exits.end();i++){
        auto in  = tree[N-1].find(*i);
        if(in != tree[N-1].end()){
            INTLINE& from = in->second;
            for(auto j = from.begin();j!=from.end();j++){
                std::stack<int> buf;
                buf.push(*i);
                outputRec(tree,res,buf,N-2,*j);
            }
        }
    }
    
    for(auto i = res.begin();i!=res.end();i++){
        std::stack<int>& buf = *i;
        std::cout<<start<<" ";
        while(!buf.empty()){
            std::cout<<dict[buf.top()]<<" ";
            buf.pop();
        }
        std::cout<<ended<<"\n";
    }
    std::cout<<"\n";
}

int main(int argc, char* argv[]){
    std::ifstream f(argv[1]);	
	std::string start, ended, dictLine,t;
	STRLINE dict;
    ROW entries;
	SET exits;
	MAT graph;
    int N = 0;
	TREE tree;
    
	getline(f, start);
	getline(f, ended);
	getline(f, dictLine);
	
	std::stringstream iss(dictLine);
	while(iss>>t) dict.push_back(t);
	f.close();
	
	init(start, ended, dict, entries, exits, graph,N);
	if(iterate(entries, exits, graph,N, tree))
		output(start, ended, dict, exits,tree);
    return 0;
}