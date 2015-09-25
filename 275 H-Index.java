/*
H-Index II
https://leetcode.com/problems/h-index-ii/
*/
public class Solution {
    public int hIndex(int[] citations) {
        int lt = 0;
        int rt = citations.length - 1;
        int hIndex = 0;
        
        while(lt <= rt){
            int pivot = (lt + rt >> 1);
            if (citations[pivot] >= citations.length - pivot) {
                hIndex = citations.length - pivot;
                rt = pivot - 1;
            }
            else
                lt = pivot + 1;
        }
        
        return hIndex;
    }
}
