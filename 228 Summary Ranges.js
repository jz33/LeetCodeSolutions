/*
Summary Ranges
https://leetcode.com/problems/summary-ranges/
*/
/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    var i,p,lt;
    var r = [];
    if(nums.length === 0) return r;
    lt = p = nums[0];
    for(i = 1;i<nums.length;i++){
        if(nums[i] === p + 1){
            p++;
        } else {
            if(lt === p){
                r.push(p.toString());
            } else {
                r.push(lt + "->" + p);
            }
            lt = p = nums[i];
        }
    }
    if(lt === p){
        r.push(p.toString());
    } else {
        r.push(lt + "->" + p);
    }
    return r; 
};
