#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
/*
207 Course Schedule
https://leetcode.com/problems/course-schedule/
*/
#define MAKE(a,b) std::make_pair(a,b)
#define DEBUG 1

typedef std::pair<int, int> Pair;
typedef std::unordered_set<int> Uset;
typedef std::unordered_map<int, Uset> Graph;

// print procedure if @ 210
bool compute(int numCourses, std::vector<Pair>& in)
{
    /*
    count parents. 0 : no parents
    */
    std::vector<int> ref(numCourses, 0);
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

        Uset& cands = graph[from];
        for (auto i = cands.begin(); i != cands.end(); i++)
        {
            if (ref[*i] == 1)
            {
                reached++;
                dq.push_back(*i);
            }
            else
                ref[*i]--;
        }
    }

    if (DEBUG)
    {
        std::cout << "ref: \n";
        for (int i = 0; i<numCourses; i++)
            std::cout << ref[i] << " ";
        std::cout << "\n";
    }
    return reached == numCourses;
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
    int numCourses = 10;
    std::string raw = "[[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]";
    
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
    std::cout << compute(numCourses, in) << "\n";
}
int main()
{
    test();
    return 0;
}
