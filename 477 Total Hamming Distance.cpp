/*
477. Total Hamming Distance
https://leetcode.com/problems/total-hamming-distance/
*/
int totalHammingDistance(vector<int>& nums) {
      int buf[32];
      for(int i = 0;i<32;i++){
          buf[i] = 0;
      }
      int x;
      for(auto i = nums.begin();i!=nums.end();i++) {
          x = *i;
          int mask = 1;
          for(int j = 0;j<32;j++) {
              if(x & mask) {
                  buf[j]++;
              }
              mask <<= 1;
          }
      }
      int total = 0;
      int n = nums.size();
      for(int i = 0;i<32;i++){
          total += buf[i] * (n - buf[i]);
      }
      return total;
  }
