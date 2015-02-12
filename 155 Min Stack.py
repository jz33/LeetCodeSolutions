import random,sys
'''
155 Min Stack
https://oj.leetcode.com/problems/min-stack/

Using 2 stacks
'''
def randomList(size = 8):
    ls = []
    for i in range(0,size):
        ls.append(random.randint(1,size*2));
    return ls
            
class min_stack:
    def __init__(self):
        self.contents = []
        self.minimums = []
        self.minValue = sys.maxint

    def push(self, e):
        self.contents.append(e)
        if e <= self.minValue:
            self.minimums.append(e)
            self.minValue = e

    def pop(self):
        if len(self.contents) == 0:
            raise Exception("len(self.contents) == 0")
        
        e = self.contents.pop()
        if e == self.minValue:
            self.minimums.pop()
            self.minValue = self.minimums[-1] \
                            if len(self.minimums) > 0 \
                            else sys.maxint
        return e
        
    def top(self):
        if len(self.contents) == 0:
            raise Exception("len(self.contents) == 0")      
        return self.contents[-1]
    ''' 
    def minValue(self):
        return self.minValue
    '''
    def empty(self):
        return True if len(self.contents) == 0 else False
    
    def dump(self):
        print "contents: ", len(self.contents), self.contents
        print "minimums: ", len(self.minimums), self.minimums
        print "minValue: ", self.minValue
    
def main():
    ms = min_stack()
    ls = randomList()
    for i in range(0,len(ls)):
        ms.push(ls[i])
    ms.dump()
    while not ms.empty():
        print ms.pop(), ms.minValue
    ms.dump()
    
if __name__ == "__main__":
    main()
