/*
1268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/

Given an array of strings products and a string searchWord.
We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
*/
class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        List<List<String>> res = new ArrayList<>();
        Arrays.sort(products);
        int startIndex = 0;
        for (int i = 0; i < searchWord.length(); ++i) {
            List<String> row = new ArrayList<>();
            if (startIndex != -1) {
                String prefix = searchWord.substring(0, i + 1);
                startIndex = lowerBound(products, prefix);
                if (startIndex != -1) {
                    for (int j = startIndex; j < startIndex + 3 && j < products.length; ++j) {
                        String cand = products[j];
                        if (cand.startsWith(prefix)) {
                            row.add(cand);
                        }
                    }
                }
            }
            res.add(row);
        }
        return res;
    }
    
    private int lowerBound(String[] arr, String target) {
        int bound = -1;
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            String midStr = arr[mid];
            if (midStr.startsWith(target) || target.compareTo(midStr) < 0) {
                bound = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return bound;
    }
}
