'''
588. Design In-Memory File System
https://leetcode.com/problems/design-in-memory-file-system/

Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:
    FileSystem() Initializes the object of the system.
    List<String> ls(String path)
        If path is a file path, returns a list that only contains this file's name.
        If path is a directory path, returns the list of file and directory names in this directory.
    The answer should in lexicographic order.
    void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
    void addContentToFile(String filePath, String content)
        If filePath does not exist, creates that file containing given content.
        If filePath already exists, appends the given content to original content.
    String readContentFromFile(String filePath) Returns the content in the file at filePath.

Example 1:

Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"

Constraints:
    1 <= path.length, filePath.length <= 100
    path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
    You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
    You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
    1 <= content.length <= 50
    At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.
'''
class Node:
    '''
    Trie node
    '''
    def __init__(self):
        self.children = {} # {directory name : node }
        self.content = None # If file, str ; not file, None
        
class FileSystem:
    def __init__(self):
        self.root = Node()

    def __getNode(self, path: str):
        node = self.root
        # Notice split can result '' strings
        subpaths = [subpath for subpath in path.split('/') if len(subpath) > 0]
        for subpath in subpaths:
            node = node.children.get(subpath)
            if not node:
                return None
        return node
    
    def __getOrCreateNode(self, path: str) -> Node:
        node = self.root
        # Notice split can result '' strings
        subpaths = [subpath for subpath in path.split('/') if len(subpath) > 0]
        for subpath in subpaths:
            if subpath not in node.children:
                node.children[subpath] = Node()
            node = node.children[subpath]
        return node
        
    def ls(self, path: str) -> List[str]:
        node = self.__getNode(path)
        if not node:
            return []
        elif node.content:
            i = path.rfind('/')
            return [path[i+1:]] # return single file
        else:
            return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.__getOrCreateNode(path)

    def addContentToFile(self, path: str, content: str) -> None:
        fileNode = self.__getOrCreateNode(path)
        if fileNode.content:
            fileNode.content += content # append to existing file
        else:
            fileNode.content = content
            
    def readContentFromFile(self, path: str) -> str:
        fileNode = self.__getNode(path)
        if fileNode and fileNode.content:
            return fileNode.content
        else:
            return ''
