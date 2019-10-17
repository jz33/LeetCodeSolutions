'''
251. Flatten 2D Vector

Design and implement an iterator to flatten a 2d vector.
It should support the following operations: next and hasNext.

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false

'''
class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.v = v
        self.x = 0
        self.y = -1
        self.move()

    def next(self) -> int:
        res = self.v[self.x][self.y]
        self.move()
        return res

    def hasNext(self) -> bool:
        return self.x < len(self.v)
    
    def move(self):
        '''
        Move x, y to next valid point
        '''
        x = self.x
        y = self.y
        v = self.v
        
        y += 1
        while x < len(v):
            if y >= len(v[x]):
                x += 1
                y = 0
            else:
                break

        self.x = x
        self.y = y
