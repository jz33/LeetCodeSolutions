package leetcode;

public class _307 extends AHelper {

    public class TreeNode {
        /**
         * 
         * @param val : value on node
         * @param lr : left bound index of array inclusive
         * @param rr : right bound index of array inclusive
         * @param lc : left child
         * @param rc : right child
         */
        public int val;
        public int lr;
        public int rr;
        public TreeNode lc;
        public TreeNode rc;

        public TreeNode(int lr, int rr) {
            this.val = 0;
            this.lr = lr;
            this.rr = rr;
            this.lc = null;
            this.rc = null;
        }
    }

    public class NumArray {
        private TreeNode root;

        private TreeNode initRec(int[] arr, int lr, int rr) {
            TreeNode node = new TreeNode(lr, rr);
            if (lr == rr)
                node.val = arr[lr];
            else {
                int mid = (lr + rr >> 1);
                node.lc = initRec(arr, lr, mid);
                node.rc = initRec(arr, mid + 1, rr);
                node.val = node.lc.val + node.rc.val;
            }
            return node;
        }

        private void updateRec(int i, int val, TreeNode node) {
            // Only update the leaves
            if (node.lr == node.rr)
                node.val = val;
            else {
                int mid = (node.lr + node.rr >> 1);
                if (i <= mid)
                    updateRec(i, val, node.lc);
                else
                    updateRec(i, val, node.rc);
                node.val = node.lc.val + node.rc.val;
            }
        }

        private int sumRangeRec(int i, int j, TreeNode node) {
            // Do not need to reach the leaves
            if (node.lr == i && node.rr == j)
                return node.val;
            else {
                int mid = (node.lr + node.rr >> 1);
                if (j <= mid)
                    return sumRangeRec(i, j, node.lc);
                else if (i >= mid + 1)
                    return sumRangeRec(i, j, node.rc);
                else
                    return sumRangeRec(i, mid, node.lc)
                            + sumRangeRec(mid + 1, j, node.rc);
            }
        }

        public NumArray(int[] nums) {
            if (nums.length == 0)
                root = null;
            else
                root = initRec(nums, 0, nums.length - 1);
        }

        void update(int i, int val) {
            if (root == null)
                return;
            updateRec(i, val, root);
        }

        public int sumRange(int i, int j) {
            if (root == null)
                return 0;
            return sumRangeRec(i, j, root);
        }
    }

    public _307() {
        super();
        int[] arr = { 1, 3, 5, 7, 9, 11 };
        NumArray sol = new NumArray(arr);
        println(sol.root.val);
        println(sol.sumRange(1, 3));
        sol.update(1, 10);
        println(sol.sumRange(1, 3));

    }

    public static void main(String[] args) {
        new _307();
    }
}
