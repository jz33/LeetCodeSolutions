'''
335 Self Crossing
https://leetcode.com/problems/self-crossing/
'''
def isSelfCrossing(dirs):
    if len(dirs) < 3: return False
    for i in xrange(3,len(dirs)):
        '''
        if intersected with i-3
        ******
             *
         *   *
         *****    
        '''
        if dirs[i] - dirs[i-2] >= 0 and dirs[i-3] - dirs[i-1] >= 0:
            return True
        '''
        if intersected with i-4       
        **  ****
        *      *
        *      *
        ********  
        '''
        if i >= 4 and dirs[i-3] - dirs[i-1] == 0 and dirs[i-2] - dirs[i-4] <= dirs[i]:
            return True
        '''
        if intersected with i-5
        *****
        *   *
        *
        *  *****
        *      *
        *      *
        ******** 
        '''
        if i >= 5 and dirs[i-3] - dirs[i-1] >= 0 and dirs[i-3] - dirs[i-1] <= dirs[i-5] \
        and dirs[i-2] - dirs[i-4] >= 0 and dirs[i-2] - dirs[i-4] <= dirs[i]:
            return True       
    return False
