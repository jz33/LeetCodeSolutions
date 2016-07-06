package leetcode;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.TreeSet;
/**
 * Largest Divisible Subset
 * https://leetcode.com/problems/largest-divisible-subset/
 * @author j.zheng
 *
 */
public class _368 {

    public void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public class Node implements Comparable<Node> {
        private int val;
        private int[] arr;

        public Node(int val, int[] arr) {
            this.val = val;
            this.arr = arr;
        }

        @Override
        public int compareTo(Node that) {
            if (that.arr.length != this.arr.length) {
                return that.arr.length - this.arr.length;
            } else {
                return that.val - this.val;
            }
        }
    }

    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        TreeSet<Node> ts = new TreeSet<Node>();
        ts.add(new Node(-1, new int[0]));
        for (int i : nums) {
            for (Node n : ts) {
                if (i % n.val == 0) {
                    int[] arr = new int[n.arr.length + 1];
                    System.arraycopy(n.arr, 0, arr, 0, n.arr.length);
                    arr[arr.length - 1] = i;
                    ts.add(new Node(i, arr));
                    break;
                }
            }
        }
        List<Integer> res = new ArrayList<Integer>();
        if (ts.size() > 0) {
            int[] arr = ts.first().arr;
            for (int i : arr) {
                res.add(i);
            }
        }
        for (Node t : ts) {
            printArray(t.arr);
        }
        return res;
    }

    public _368() {
        int[] nums = { 1, 3, 9, 18, 54, 108, 540, 90, 180, 360, 720 };
        List<Integer> res = largestDivisibleSubset(nums);
        System.out.println(res.toString());
    }

    public static void main(String args[]) {
        new _368();
    }
}
