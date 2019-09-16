/*
407. Trapping Rain Water II
https://leetcode.com/problems/trapping-rain-water-ii/

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.

Note:

Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.


After the rain, water is trapped between the blocks. The total volume of water trapped is 4
*/
#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)
#define OUT(a) std::cout<<a<<std::endl;

class WaterPoint
{
public:
   int x;
   int y;
   int h;

   WaterPoint(int x, int y, int h)
   {
      this->x = x;
      this->y = y;
      this->h = h;
   }
};

class Compare
{
public:
    bool operator() (WaterPoint a, WaterPoint b)
    {
        return a.h > b.h; 
    }
};

typedef std::priority_queue<WaterPoint,std::vector<WaterPoint>,Compare> MinHeap; 
const int VISITED = -1;

class Solution {
public:
    int pushToHeap(vector<vector<int>>& heightMap,
        MinHeap& heap,
        int height,
        int neightborX,
        int neightborY)
    {            
        // Get height of neighbor
        auto neighborHeight = heightMap[neightborX][neightborY]; 
        heightMap[neightborX][neightborY] = VISITED;
                                
        // Push in max of height and neighbor height
        heap.emplace(neightborX,neightborY,MAX(neighborHeight,height));
        
        // Return how many water can trap
        // The neighbor height must be smaller than height to trap water
        return MAX(height - neighborHeight, 0);
    }
    
    int trapRainWater(vector<vector<int>>& heightMap){
        const auto rowCount = heightMap.size(); 
        if (rowCount < 3) return 0;
        int colCount = heightMap[0].size();
        if (colCount < 3) return 0;
      
        MinHeap heap;
        
        // Push in boundries
        for (int i = 0; i < rowCount; ++i)
        {
            heap.emplace(i, 0, heightMap[i][0]);
            heightMap[i][0] = VISITED;
            
            heap.emplace(i, colCount-1, heightMap[i][colCount-1]);
            heightMap[i][colCount-1] = VISITED;
        }
        for (int j = 1; j < colCount-1; ++j)
        {
            heap.emplace(0, j, heightMap[0][j]);
            heightMap[0][j] = VISITED;
            
            heap.emplace(rowCount-1, j, heightMap[rowCount-1][j]);
            heightMap[rowCount-1][j] = VISITED;
        }
    
        // Iterate rest of the matrix
        int res = 0;
        while (!heap.empty())
        {
            auto p = heap.top();
            heap.pop();

            auto x = p.x;
            auto y = p.y;
            auto h = p.h;

            if (x+1 < rowCount-1 && heightMap[x+1][y] != VISITED)
            {
                res += pushToHeap(heightMap, heap, h, x+1, y);           
            }
            
            if (x-1 > 0 && heightMap[x-1][y] != VISITED)
            {
                res += pushToHeap(heightMap, heap, h, x-1, y);
            }
            
            if (y+1 < colCount-1 && heightMap[x][y+1] != VISITED)
            {
                res += pushToHeap(heightMap, heap, h, x, y+1);
            }
            
            if (y-1 > 0 && heightMap[x][y-1] != VISITED)
            {
                res += pushToHeap(heightMap, heap, h, x, y-1);
            }
        }
        return res;
    }
};
