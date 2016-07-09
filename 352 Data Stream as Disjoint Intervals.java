package leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

/**
 * Data Stream as Disjoint Intervals
 * https://leetcode.com/problems/data-stream-as-disjoint-intervals/
 * 
 * @author j.zheng
 *
 */
public class _352 {

    public class Interval {
        int start;
        int end;

        Interval() {
            start = 0;
            end = 0;
        }

        Interval(int s, int e) {
            start = s;
            end = e;
        }
        
        @Override
        public String toString() {
            return "[" + this.start + " " + this.end + "] ";
        }
    }

    public class ComparableInterval extends Interval implements Comparable<ComparableInterval> {

        public ComparableInterval(int s, int e) {
            super(s, e);
        }

        /**
         * Not cover case: [3 5], add [4,6]
         */
        public int compareTo(ComparableInterval that) {
            // System.out.println(this + ", " +that);
            if (this.start == this.end) {
                if (that.start == that.end) {
                    return this.start - that.start;
                } else {
                    if (this.start > that.end) {
                        return 1;
                    } else if (this.end < that.start) {
                        return -1;
                    } else {
                        return 0;
                    }
                }
            } else {
                if (that.start == that.end) {
                    if (this.start > that.end) {
                        return 1;
                    } else if (this.end < that.start) {
                        return -1;
                    } else {
                        return 0;
                    }
                } else {
                    if (this.start >= that.end) {
                        return 1;
                    } else if (this.end <= that.start) {
                        return -1;
                    } else {
                        return 0;
                    }
                }
            }
        }
    }

    private TreeSet<ComparableInterval> ts;

    public void addNum(int val) {
        ComparableInterval ci = new ComparableInterval(val, val);
        if (ts.contains(ci))
            return;

        ComparableInterval lo = ts.lower(ci);
        ComparableInterval hi = ts.higher(ci);
        int mergeSign = 0;
        if (lo != null && lo.end + 1 == val) {
            mergeSign |= 1;
        }
        if (hi != null && hi.start - 1 == val) {
            mergeSign |= 2;
        }
        switch (mergeSign) {
        case 0:
            ts.add(ci);
            break;
        case 1: // left only
            ts.remove(lo);
            ts.add(new ComparableInterval(lo.start, val));
            break;
        case 2: // right only
            ts.remove(hi);
            ts.add(new ComparableInterval(val, hi.end));
            break;
        case 3:
            ts.remove(hi);
            ts.remove(lo);
            ts.add(new ComparableInterval(lo.start, hi.end));
            break;
        default:
            break;
        }
    }

    public List<Interval> getIntervals() {
        if(ts.size() == 0) return null;
        List<Interval> res = new ArrayList<Interval>();
        for(ComparableInterval ci : ts) {
            res.add(new Interval(ci.start,ci.end));
        }
        return res;
    }

    public _352() {
        ts = new TreeSet<ComparableInterval>();
    }

    public static void dump(_352 obj) {
        List<Interval> res = obj.getIntervals();
        for (Interval j : res) {
            System.out.print(j);
        }
        System.out.println();
    }
    
    public static void test(_352 obj) {
        //int arr[] = { 1, 3, 5, 7, 9, 0, 8, 2, 4, 6, 5 };
        int arr[] = {1, 3, 7, 2, 6, 3};
  
        dump(obj);
        for (int i : arr) {
            obj.addNum(i);
            dump(obj);
        }
        //dump(obj);
    }

    public static void main(String[] args) {
        _352 obj = new _352();
        test(obj);
    }
}
