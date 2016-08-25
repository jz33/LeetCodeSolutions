#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
/*
Longest Absolute File Path
https://leetcode.com/problems/longest-absolute-file-path/
*/
int lengthLongestPath(std::string src) {
    src += "\n";
    int size = (int)src.size();

    std::vector<int> vec;
    vec.push_back(0);
    int maxSize = 0;
    int j = 0;
    int i = 0;
    int indents = 0;
    bool foundDot = false;
    while (i < size) {
        // found file
        if (src[i] == '.') {
            foundDot = true;
            i++;
        }
        // found \n
        else if (src[i] == '\n') {
            int curr = vec[indents] + i - j;
            if (foundDot)
            {
                maxSize = std::max(maxSize, curr);
                foundDot = false;
            }
            if (indents + 1 >= vec.size()) {
                vec.push_back(curr+1);
            }
            else {
                vec[indents + 1] = curr+1;
            }
            i += 1;

            //find \t
            indents = 0;
            while (i < size && src[i] == '\t') {
                indents++;
                i += 1;
            }
            j = i;
        }
        else {
            i++;
        }
    }
    return maxSize;
}

