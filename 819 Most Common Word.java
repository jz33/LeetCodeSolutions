class Solution {
    public String mostCommonWord(String helpText, String[] wordsToExclude) {
        HashSet<String> bannedSet = new HashSet<>();
        for (String word : wordsToExclude) {
            if (!word.isEmpty()) {
                bannedSet.add(word.toLowerCase());
            }
        }

        HashMap<String, Integer> histogram = new HashMap<>();
        int highestCount = 0;

        String[] words = helpText.toLowerCase().split("[\\p{Punct}\\s]+");
        for (String word : words) {
            if (!bannedSet.contains(word)) {
                int newCount = histogram.getOrDefault(word, 0) + 1;
                histogram.put(word, newCount);
                highestCount = Math.max(highestCount, newCount);
            }
        }
        
        for (Map.Entry<String, Integer> e : histogram.entrySet()) {
            if (e.getValue() == highestCount) {
                return e.getKey();
            }
        }
        return "";
    }
}
