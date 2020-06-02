/*
937 Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/

You have an array of logs.  Each log is a space delimited string of words.
For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
The digit-logs should be put in their original order.
Return the final order of the logs.

Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
*/

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        std::stable_sort(logs.begin(), logs.end(), [&](const auto& a, const auto& b) -> bool{
            // Notice this lambda funtion should return true if a is smaller than b
            
            const auto isad = isDigitLog(a);
            if (isad) {
                // If a is digit, b is digit, a is not smaller than b;
                // If a is digit, b is letter, a is bigger than b;
                return false;
            }

            const auto isbd = isDigitLog(b);
            if (isbd) {
                // If a is letter, b is digit, a is smaller than b
                return true;
            }

            const auto [ia, ca] = splitLetterLog(a);
            const auto [ib, cb] = splitLetterLog(b);
            const auto cmp = ca.compare(cb);
            if (cmp < 0) {
                return true;
            } else if (cmp > 0) {
                return false;
            }

            return ia.compare(ib) < 0;
            
        });
        
        return logs;
    }
    
private:
    bool isDigitLog(string log) {
        auto i = log.find(' ');
        auto c = log[i+1];
        return '0' <= c && c <= '9';
    }
    
    std::pair<string, string> splitLetterLog(string log) {
        auto i = log.find(' ');
        auto id = log.substr(0, i);
        auto content = log.substr(i+1);
        return {id, content};
    }
};
