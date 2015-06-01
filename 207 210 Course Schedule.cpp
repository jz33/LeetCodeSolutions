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

A standard deep-first traversal

At start, nodes are divided into 2 groups,
"root nodes", who has no dependences,
"inner nodes", who has dependences.

If "one node is reachable if one of its parent is reached",
then all inner nodes are reachable if and only
if at least 1 root node is pointed to at least
1 inner node. This is very simple.

Else if "one node is reachable only if all of its parents are reached",
then the problem is to find whether the graph has cycle
*/
#define MAKE(a,b) std::make_pair(a,b)
#define DEBUG 1

typedef std::pair<int, int> Pair;
typedef std::unordered_set<int> Uset;
typedef std::unordered_map<int, Uset> Graph;

// print dfs procedure if @ 210
bool dfs(int numCourses, std::vector<Pair>& in)
{
	/*
	-1 : not reached yet
	0 : starting node
	1 : reached
	*/
	std::vector<int> ref(numCourses, 0);
	Graph graph;

	// initialize starting nodes, graph
	int togo, from;
	for (auto i = in.begin(); i != in.end(); i++)
	{
		togo = i->first;
		from = i->second;

		ref[togo] = -1;
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

	// dfs
	while (!dq.empty() && reached != numCourses)
	{
		from = dq.front();
		dq.pop_front();

		Uset& cands = graph[from];
		for (auto i = cands.begin(); i != cands.end(); i++)
		{
			if (ref[*i] == -1)
			{
				ref[*i] = 1;
				reached++;
				dq.push_back(*i);
			}
            // if ref[*i] == 1, cycle !
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
int main()
{
	int numCourses = 4;
	std::vector<Pair> in;
	in.push_back(MAKE(1, 0));
	in.push_back(MAKE(2, 0));
	in.push_back(MAKE(3, 1));
	in.push_back(MAKE(3, 2));

	std::cout << dfs(numCourses, in) << "\n";

	in.clear();
	in.push_back(MAKE(1, 0));
	in.push_back(MAKE(2, 1));
	in.push_back(MAKE(1, 3));

	std::cout << dfs(numCourses, in) << "\n";

	return 0;
}
