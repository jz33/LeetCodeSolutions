public class Solution {
    public int coinChange(int[] coins, int amount) {
        int size = amount + 1;
        int[] buf = new int[size];
        for(int i = 1;i<size;i++){
            buf[i] = size; // a max value
        }
        for(int c : coins){
            for(int i = c;i<size;i++){
                buf[i] = Math.min(buf[i],buf[i-c] + 1);
            }
        }
        return buf[amount] == size ? -1 : buf[amount];
    }
}
