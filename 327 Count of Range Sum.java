/*
lt     mid      rt
0 1 2 3 4 5 6 7
*/
public int merge(long[] arr, long[] buf, int lt, int mid, int rt, int lower, int upper){
    int lo = mid; // first index arr[lo] - arr[i] >= lower
    int up = mid; // first index arr[up] - arr[i] > upper
    int inv = 0;

    for(int i = lt, j = mid, b = lt;i < mid;i++){
        long vi = arr[i];
        
        while(lo < rt && arr[lo] - vi <  lower) lo++;
        while(up < rt && arr[up] - vi <= upper) up++;
        inv += up - lo;
        
        while(j < rt && arr[j] <= vi) buf[b++] = arr[j++];
        buf[b++] = vi;
    }
    
    System.arraycopy(buf,lt,arr,lt,rt-lt);
    println(inv);
    return inv;
}

public int countRangeSum(int[] nums, int lower, int upper) {
    int length = nums.length;
    long[] arr = new long[length+1];
    long s = 0;
    for(int i = 0;i<length;i++){
        s += nums[i];
        arr[i+1] = s;
    }
    length++;
    
    long[] buf = new long[length];
    System.arraycopy(arr,0,buf,0,length);
    
    int inv = 0;
    int bound = length * 2;
    for(int stride = 2; stride < bound; stride <<= 1){
        for(int lt = 0;lt<length;lt += stride){
            int mid = Math.min(lt + (stride >> 1),length);
            int rt  = Math.min(lt + stride,length);
            inv += merge(arr,buf,lt,mid,rt,lower,upper);
        }
    }
    return inv;
}
