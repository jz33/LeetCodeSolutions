#include <iostream>
#include <vector>
#include <queue>

typedef std::vector<int> VEC;
typedef std::vector<VEC> MAT;

#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)
#define OUT(a) std::cout<<a<<std::endl
#define DEBUG 1

void dumpVec(VEC v) {
    if(DEBUG) {
        for(auto i = v.begin();i!=v.end();i++) {
        std::cout<<*i<<" ";
        }
        std::cout<<std::endl;
    }   
}

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

int trapRainWater(MAT& heightMap){
    int RC = heightMap.size(); // row count
    if (RC == 0) return 0;
    int CC = heightMap[0].size(); // column count
    if (CC == 0) return 0;
    
    /*
    How to implement min heap in C++?
    */
    auto comp = [](WaterPoint& a, WaterPoint& b) { return a.h > b.h; };
    std::priority_queue<WaterPoint,std::vector<WaterPoint>,decltype(comp)> heap(comp);

    // construct visited matrix
    MAT visited(RC, VEC(CC,0));

    // push in boundries
    for(int i=0;i<RC;i++){
        for(int j=0;j<CC;j++){
            if (i == 0 || j == 0 || i == RC-1 || j == CC-1){
                heap.push(WaterPoint(i,j,heightMap[i][j]));
                visited[i][j] = 1;
            }         
        }
    }

    // iterate heap
    int res = 0;
    while(!heap.empty()){
        auto p = heap.top();
        heap.pop();

        auto x = p.x;
        auto y = p.y;
        auto h = p.h;

        if(x+1 < RC-1 && visited[x+1][y] == 0){
            res += MAX(h-heightMap[x+1][y],0);
            // push in either water height or building height 
            heap.push(WaterPoint(x+1,y,MAX(heightMap[x+1][y],h)));
            visited[x+1][y] =1;
        }
        if(x-1 > 0 && visited[x-1][y] == 0){
            res += MAX(h-heightMap[x-1][y],0);
            // push in either water height or building height 
            heap.push(WaterPoint(x-1,y,MAX(heightMap[x-1][y],h)));
            visited[x-1][y] =1;
        }
        if(y+1 < CC-1 && visited[x][y+1] == 0){
            res += MAX(h-heightMap[x][y+1],0);
            // push in either water height or building height 
            heap.push(WaterPoint(x,y+1,MAX(heightMap[x][y+1],h)));
            visited[x][y+1] =1;
        }
        if(y-1 > 0 && visited[x][y-1] == 0){
            res += MAX(h-heightMap[x][y-1],0);
            // push in either water height or building height 
            heap.push(WaterPoint(x,y-1,MAX(heightMap[x][y-1],h)));
            visited[x][y-1] =1;
        }
    }

    return res;
}

/*
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
*/
void test0(void) {
    MAT mat;  
    mat.push_back(VEC{1,4,3,1,3,2});
    mat.push_back(VEC{3,2,1,3,2,4});
    mat.push_back(VEC{2,3,3,2,3,1});
    std::cout<<trapRainWater(mat)<<std::endl;
}
/*
[[12,13,1,12],
[13,4,13,12],
[13,8,10,12],
[12,13,12,12],
[13,13,13,13]]
*/
void test1(void) {
    MAT mat;
    mat.push_back(VEC{12,13, 1,12});
    mat.push_back(VEC{13, 4,13,12});
    mat.push_back(VEC{13, 8,10,12});
    mat.push_back(VEC{12,13,12,12});
    mat.push_back(VEC{13,13,13,13});
    std::cout<<trapRainWater(mat)<<std::endl;
}

int main() {
    test0();
    test1();
    return 0;
}

