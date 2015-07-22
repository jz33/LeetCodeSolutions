#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
/*
Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
*/
#define MAKE(a,b) std::make_pair(a,b)
#define DEBUG 1

typedef std::vector<int> Vec;
typedef std::pair<int, int> Pair;
typedef std::unordered_set<int> Uset;
typedef std::unordered_map<int, Uset> Graph;

template<typename T>
void dump(T& a)
{
    for(auto i = a.begin();i!=a.end();i++) printf("%d ",*i);
    printf("\n");
}

// print procedure if @ 210
Vec compute(int numCourses, std::vector<Pair>& in)
{
    /*
    count parents. 0 : no parents
    */
    Vec ref(numCourses, 0);
    
    Vec seq;
    Graph graph;

    // initialize starting nodes, graph
    int togo, from;
    for (auto i = in.begin(); i != in.end(); i++)
    {
        togo = i->first;
        from = i->second;

        ref[togo]++;
        graph[from].insert(togo);
    }

    // gather starting nodes
    std::deque<int> dq;
    int reached = 0;
    for (int i = 0; i<numCourses; i++){
        if (ref[i] == 0){
            dq.push_back(i);
            reached++;
        }
    }

    // bfs
    while (!dq.empty())
    {
        from = dq.front();
        dq.pop_front();
        seq.push_back(from);

        Uset& cands = graph[from];
        for (auto i = cands.begin(); i != cands.end(); i++)
        {
            if (ref[*i] == 1)
            {
                reached++;
                if(reached > numCourses)
                {
                    // Cycle!
                    dq.clear();
                    break;
                }
                dq.push_back(*i);
            }
            else
                ref[*i]--;
        }
    }

    if (DEBUG)
    {
        std::cout << "ref: \n";
        dump<Vec>(ref);
    }
    
    if(reached != numCourses)
        seq.clear();
    
    return seq;
}
void removeDuplicates(std::vector<Pair>& in)
{
    if(in.size() < 2) return;

    std::set<Pair> filter;
    for (auto i = in.begin(); i != in.end(); i++)
        filter.insert(*i);

    size_t j = 0;
    for (auto i = filter.begin(); i != filter.end(); i++)
        in[j++] = *i;

    in.resize(j);
    in.shrink_to_fit();
}
void test(void)
{
    int numCourses = 4;
    //std::string raw = "[[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]";
    
    std::string raw = "[[1,0],[2,0],[3,1],[3,2]";
    
    std::replace(raw.begin(),raw.end(),',',' ');
    std::replace(raw.begin(),raw.end(),'[',' ');
    std::replace(raw.begin(),raw.end(),']',' ');
    
    std::vector<Pair> in;
    std::istringstream iss(raw);
    int togo, from;
    
    while(iss>>togo){
        iss>>from;
        in.push_back(MAKE(togo, from));
    }

    removeDuplicates(in);
    Vec seq = compute(numCourses, in);
    dump<Vec>(seq);
}
int main()
{
    test();
    return 0;
}
