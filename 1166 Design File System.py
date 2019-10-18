'''
1166. Design File System
https://leetcode.com/problems/design-file-system/

You are asked to design a file system which provides two functions:

createPath(path, value): Creates a new path and associates a value to it if possible and returns True.
Returns False if the path already exists or its parent path doesn't exist.

get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters.
For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Implement the two functions.

Please refer to the examples for clarifications.

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1

Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.children = {} # route : Node
    
class FileSystem:
    def __init__(self):
        self.root = Node(None)

    def createPath(self, path: str, value: int) -> bool:        
        # Be careful! Python string split contains empty strings!
        paths = path.split('/')
        
        n = self.root
        for i, s in enumerate(paths):
            if not s:
                continue
            if s in n.children:
                if i == len(paths) - 1:
                    # path already existed
                    return False
                else:
                    n = n.children[s]
            else:
                if i == len(paths) - 1:
                    n.children[s] = Node(value)
                else:
                    # parent path does not exist
                    return False
        return True
            
    def get(self, path: str) -> int:
        n = self.root
        paths = path.split('/')
        for i, s in enumerate(paths):
            if not s:
                continue
                
            if s in n.children:
                n = n.children[s]
            else:
                # path does not exist
                return -1
            
        return n.value
