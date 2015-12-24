package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes){
        Arrays.sort(primes);
        int size = primes.length;
        List<Integer> uglies = new ArrayList<Integer>(Arrays.asList(new Integer[]{1}));
        int[] pointers = new int[size];
        int[] results  = new int[size];

        n--;
        for(int i = 0;i<n;i++){
            int mr = Integer.MAX_VALUE; // min result
            for(int j = 0;j<size;j++){
                int r = uglies.get(pointers[j]) * primes[j];
                mr = Math.min(mr,r);
                results[j] = r;
            }
            uglies.add(mr);

            for(int j = 0;j<size;j++){
                if(mr == results[j])
                    pointers[j]++;
            }
        }
        return uglies.get(uglies.size()-1);
    }
}
