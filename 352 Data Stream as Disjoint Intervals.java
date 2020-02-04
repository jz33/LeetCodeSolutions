/*
352. Data Stream as Disjoint Intervals
https://leetcode.com/problems/data-stream-as-disjoint-intervals/

Given a data stream input of non-negative integers a1, a2, ..., an, ...,
summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ...,
then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]

Follow up:

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
*/
class SummaryRanges {
    
    public class Interval implements Comparable<Interval>{	
        int left;	
        int right;	

        Interval(int left, int right) {	
            this.left = left;
            this.right = right;
        }	

        @Override	
        public int compareTo(Interval that) {
            
            // If 2 intervals are overlapped, consider they are identical
            if (Math.max(this.left, that.left) <= Math.min(this.right, that.right)) {
                return 0;
            }
            return this.left - that.left;
        }	
    }

    public TreeSet<Interval> container;
    
    /** Initialize your data structure here. */
    public SummaryRanges() {
        container = new TreeSet<Interval>();
    }
    
    public void addNum(int val) {
        Interval mid = new Interval(val, val);
        if (container.contains(mid)) {
            return;
        }
        
        Interval lo = container.lower(mid); // stricly lower than
        Interval up = container.higher(mid); // stricly highter than
        
        int left = val;
        int right = val;
        
        if (lo != null && lo.right + 1 == val)
        {   
            left = lo.left;
            container.remove(lo);
        }
        if (up != null && up.left - 1 == val)
        {   
            right = up.right;
            container.remove(up);
        }
       
        container.add(new Interval(left, right)); 
    }
    
    public int[][] getIntervals() {
        int[][] res = new int[container.size()][2];
        int i = 0;
        for(Interval it : container) {	
            res[i][0] = it.left;
            res[i][1] = it.right;
            i++;
        }	
        return res;
    }
}
