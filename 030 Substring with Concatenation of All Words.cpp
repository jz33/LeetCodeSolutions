#define ERROR "###"
#define ENDLINE std::cout<<"\n"

typedef std::unordered_map<std::string, int> MAP;

template<typename T>
void dump(T& iterable)
{
    for(auto i = iterable.begin();i!=iterable.end();i++)
        std::cout<<*i<<" ";
    ENDLINE;
}

void dumpMap(MAP& m)
{
    for(auto i = m.begin();i!=m.end();i++)
        std::cout<<i->first<<" : " <<i->second<<"\n";
    ENDLINE;
}

class Solution {
public:
    /*
    O(n) method
    */
    std::vector<int> findSubstring(std::string src, std::vector<std::string>& words)
    {
        std::vector<int> res;
        size_t width = words[0].size();
        if(words.size() == 0 || width == 0) return res;
        if(width * words.size() > src.size()) return res;
        
        MAP book; // {word: appearance cound}
        for(auto i = words.begin();i!=words.end();i++)
        {
            book[*i]++;
        }  
        
        // record appearance of substrings for quick reference
        std::vector<std::string> apps(src.size() - width + 1, ERROR); // {int: word/ERROR}
        for(size_t i = 0;i < src.size() - width + 1;i++)
        {
            auto sub = src.substr(i,width);
            if(book.find(sub) != book.end())
                apps[i] = sub;
        }

        // O(n)
        for(size_t i = 0;i < width;i++)
        {
            MAP record; // record current valid substrings
            size_t found = 0; // how many strings are found now
            size_t left = i; // left start point of valid substring
            for(size_t j = i;j < src.length() - width + 1;j += width)
            {
                auto& sub = apps[j];
                
                // if current substring is in book
                if(sub != ERROR) 
                {
                    // check if sub is redundant
                    if(record.find(sub) != record.end() && record[sub] == book[sub])
                    {
                        // shrink from left
                        auto& leftStr = apps[left];

                        // if left string is not same as redundant
                        while(leftStr.compare(sub) != 0)
                        {                         
                            record[leftStr]--;
                            found--;
                            left += width;                                
                            leftStr = apps[left];
                        }
                        // left points to next string of redundant
                        left += width;
                    }
                    else
                    {
                        // valid substring
                        record[sub]++;
                        found++;
                    }
                    
                    // try update result
                    if(found == words.size())
                    {
                        res.push_back(left);
                    }
                }
                else
                {
                    // reset
                    record.clear();
                    found = 0;                   
                    left = j + width;
                }
            }
        }
        return res;   
    }
};
