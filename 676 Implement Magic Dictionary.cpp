typedef std::vector<std::string> VEC;
typedef std::unordered_set<std::string> SET;
typedef std::unordered_map<std::string,SET> MAP;
/*
https://leetcode.com/problems/implement-magic-dictionary
*/
class MagicDictionary {
public:
    /** Initialize your data structure here. */
    MagicDictionary() {
        book.clear();
    }
    
    /** Build a dictionary through a list of words */
    void buildDict(std::vector<string> words) {
        for(auto& word : words) {
            for(auto i = 0;i<word.size();i++) {
                auto ns = word.substr(0,i) + "*" + word.substr(i+1); // won't throw
                auto ls = book.find(ns);
                if (ls == book.end()) {
                    SET vs {word};
                    book[ns] = vs;
                } else {
                    ls->second.insert(word);
                }
            }
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(std::string word) {
        for(auto i = 0;i<word.size();i++) {
            auto ns = word.substr(0,i) + "*" + word.substr(i+1);
            auto ls = book.find(ns);
            if (ls != book.end()) {
                for (auto& s : ls->second) {
                    if(s != word) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
private:
    
    MAP book;
    
};



/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * bool param_2 = obj.search(word);
 */
