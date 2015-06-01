#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <unordered_set>
#include <unordered_map>
/*
207 Course Schedule
210 Course Schedule II
https://leetcode.com/problems/course-schedule/
https://leetcode.com/problems/course-schedule-ii/

This is assumed that "1 node is reachable only if
ALL parent nodes are reached", then a standard
breath-first traversal is used to detect cycle.

If condition is "1 node is reachable if
1 of its parent nodes is reached", detecting cycle
is unnecessary
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
void test(void)
{
    int numCourses = 4;
    std::vector<Pair> in;
    in.push_back(MAKE(1, 0));
    in.push_back(MAKE(2, 0));
    in.push_back(MAKE(3, 1));
    in.push_back(MAKE(3, 2));

    std::cout << compute(numCourses, in) << "\n";

    in.clear();
    in.push_back(MAKE(1, 0));
    in.push_back(MAKE(2, 1));
    in.push_back(MAKE(3, 2));
    in.push_back(MAKE(1, 3));

    std::cout << compute(numCourses, in) << "\n";

    in.clear();
    in.push_back(MAKE(2, 1));
    in.push_back(MAKE(3, 2));
    in.push_back(MAKE(1, 3));

    std::cout << compute(numCourses, in) << "\n";
}
int main()
{
    test();
    return 0;
}
