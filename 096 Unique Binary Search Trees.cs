/*
096 Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/
*/
public int NumTrees(int n) {
      // [buckle size[buckle count]]
      // mat[i][j] means total trees with size i+1, stars from j+1
      var mat = new List<int[]>(); 
      var row = Enumerable.Repeat(1, n).ToArray();
      mat.Add(row);
      for (int i = 1; i < n; i++)
      {
          row = Enumerable.Repeat(0, n-i).ToArray();
          for (int j = 0; j < n-i;j++)
          {
              var a = mat[i - 1][j+1];
              for (int k = j + 1; k < j + i; k++)
              {
                  a += mat[k - j - 1][j] * mat[j+i-k-1][k+1];
              }
              a += mat[i - 1][j];
              row[j] = a;
          }
          mat.Add(row);
      }
      return mat[n - 1][0];
  }
