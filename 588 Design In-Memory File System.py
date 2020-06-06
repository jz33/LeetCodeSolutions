'''
588. Design In-Memory File System
https://leetcode.com/problems/design-in-memory-file-system/

Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name.
If it is a directory path, return the list of file and directory names in this directory.
Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path.
If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format.
If the file doesn't exist, you need to create that file containing given content.
If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.
'''
class Node:
    def __init__(self, isFile = False):
        self.isFile = isFile # is file or directory
        self.children = {} # {directory name : node }
        self.content = None # file content
        
class FileSystem:
    def __init__(self):
        self.root = Node()

    def getNode(self, path: str) -> Node:
        '''
        Private
        Get the node with given path.
        Return None if node not existed.
        '''
        node = self.root
        subs = [s for s in path.split('/') if len(s) > 0] # notice split can have '' strings
        for sub in subs:
            node = node.children.get(sub)
            if not node:
                return None
        return node
    
    def createNode(self, path: str) -> Node:
        '''
        Private
        Get the node with give path.
        If direcotyr not existed, create. Return leaf node
        '''
        node = self.root
        subs = [s for s in path.split('/') if len(s) > 0] # notice split can have '' strings
        for sub in subs:
            if sub not in node.children:
                node.children[sub] = Node()
            node = node.children[sub]
        return node
        
    def ls(self, path: str) -> List[str]:
        node = self.getNode(path)
        if not node:
            return []
        elif node.isFile:
            i = path.rfind('/')
            return [path[i+1:]] # [filename]
        else:
            return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.createNode(path)

    def addContentToFile(self, path: str, content: str) -> None:
        fileNode = self.createNode(path)
        if fileNode.isFile:
            fileNode.content += content # append to existing file
        else:
            fileNode.isFile = True # new file
            fileNode.content = content
            
    def readContentFromFile(self, path: str) -> str:
        fileNode = self.getNode(path)
        if fileNode and fileNode.isFile:
            return fileNode.content
        else:
            return ''
