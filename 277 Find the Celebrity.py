'''
277. Find the Celebrity
https://leetcode.com/problems/find-the-celebrity/

Suppose you are at a party with n people labeled from 0 to n - 1 and among them,
there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know the celebrity,
but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
You are only allowed to ask questions like:
"Hi, A. Do you know B?" to get information about whether A knows B.

You need to find out the celebrity (or verify there is not one)
by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) that tells you whether a knows b.
Implement a function int findCelebrity(n).
There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

Example 1:

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:

Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

Constraints:
    n == graph.length == graph[i].length
    2 <= n <= 100
    graph[i][j] is 0 or 1.
    graph[i][i] == 1

Follow up: If the maximum number of allowed calls to the API knows is 3 * n,
could you find a solution without exceeding the maximum number of calls?

'''
# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass

class Solution:
    def findCelebrity(self, n: int) -> int:
        # 1. Guess the celebrity by iterate n people
        celebrity = 0
        for people in range(1, n):
            if knows(celebrity, people):
                celebrity = people
        
        # 2. Verify that celebrity knows no others
        # Only needs to verify 0 ... celebrity-1 people, as later people
        # are already verified in #1
        if any(knows(celebrity, people) for people in range(celebrity)):
            return -1
        
        # 3. Verify that everyone knows this celebrity
        if any(people != celebrity and not knows(people, celebrity) for people in range(n)):
            return -1
        
        return celebrity
