/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var reverse = function(arr,lt,rt)
{
    var t = 0;
    while(lt < rt)
    {
        t = arr[lt];
        arr[lt] = arr[rt];
        arr[rt] = t;
        lt++;
        rt--;
    }
}
var rotate = function(arr, k) {
    var n = arr.length;
    if(n === 0);
    k = k % n;
    if(k === 0) return;
    reverse(arr,0,n - 1);
    reverse(arr,0,k-1);
    reverse(arr,k,n - 1);
};
