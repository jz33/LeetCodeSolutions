/*
Repeated DNA Sequences 
https://leetcode.com/problems/repeated-dna-sequences/

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
*/
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {  
        vector<string> res;
        std::unordered_map<int, int> counter; // {hash : count}
        int hash = 0;
        for (size_t i = 0; i < s.size(); ++i) {
            char c = s[i];
            
            /*
            Minus 64       Binary   &6   >>1
            'A' - 64 : 1 : 00001 : 001 :  00
            'C' - 64 : 3 : 00011 : 011 :  01
            'G' - 64 : 7 : 00111 : 111 :  11
            'T' - 64 :20 : 10100 : 100 :  10
            */
            int newHash = ((c - 64) & 6) >> 1;
            
            // Accumulate hash by 2 bits, and clip into 20 bits
            hash = ((hash << 2) | newHash) & 0xFFFFF;
            
            if (i >= 9) {
                if (counter[hash] == 1) {
                    res.emplace_back(s.substr(i - 9, 10));
                    counter[hash] = 2;
                } else if(counter[hash] == 0) {
                    counter[hash] = 1;
                }
            }       
        }
        return res;
    }
};
