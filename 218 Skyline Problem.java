class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<int[]> heights = new ArrayList<>();
        for (int[] b: buildings) {
            heights.add(new int[]{b[0], -b[2]});
            heights.add(new int[]{b[1], b[2]});
        }
        
        // Sort by location then height
        Collections.sort(heights, (a, b) -> (a[0] == b[0]) ? a[1] - b[1] : a[0] - b[0]);
        
        // Max TreeMap, stores {heights : count}
        TreeMap<Integer, Integer> heightMap = new TreeMap<>(Collections.reverseOrder());
        heightMap.put(0,1);
        
        int prevHeight = 0;
        List<List<Integer>> skyLine = new ArrayList();
        for (int[] h: heights) {
            if (h[1] < 0) {
                // Put in height for new building
                Integer ctr = heightMap.getOrDefault(-h[1], 0);
                heightMap.put(-h[1], ctr + 1);
            } else {
                // Remove finished building
                Integer ctr = heightMap.get(h[1]);
                if (ctr == 1) {
                    heightMap.remove(h[1]);
                } else {
                    heightMap.put(h[1], ctr - 1);
                }
            }
            
            int maxHeight = heightMap.firstKey();
            if (maxHeight != prevHeight) {
                skyLine.add(Arrays.asList(h[0], maxHeight));
                prevHeight = maxHeight;
            }
        }
        return skyLine;
    }
}
