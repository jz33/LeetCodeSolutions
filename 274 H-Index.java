/**
 * H-index I
 * https://leetcode.com/problems/h-index/
 */
public class Solution {
    
    private java.util.Random rd = new java.util.Random();
    
    public void swap(int[] arr, int lt, int rt){
        int i = arr[lt];
        arr[lt] = arr[rt];
        arr[rt] = i;
    }
    
    public int partition(int[] arr, int lt, int rt) {
        
        int pivot = rd.nextInt(rt - lt + 1) + lt; // [lt,rt]
        int pivot_val = arr[pivot];
        int new_pivot = lt;

        swap(arr,pivot,rt);
        for(int i = lt;i<=rt;i++){
            if(arr[i] < pivot_val){
                swap(arr,i,new_pivot++);
            }
        }
        swap(arr,new_pivot,rt);
        return new_pivot;
    }

    /**
     * Quickselect
     * Search the smallest i that citation[i] >= N - i
     * @param citations
     * @return h index
     */   
    public int hIndex(int[] citations) {
        int lt = 0;
        int rt = citations.length - 1;
        int hIndex = 0;
        while (lt <= rt) {
            int pivot = partition(citations, lt, rt);
            if (citations[pivot] >= citations.length - pivot) {
                hIndex = citations.length - pivot;
                rt = pivot - 1;
            } else
                lt = pivot + 1;
        }
        return hIndex;
    }
}
