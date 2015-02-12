'''
134 Gas Station
https://oj.leetcode.com/problems/gas-station/
'''  
def peak(gas,cost):
    if len(gas) != len(cost):
        raise Exception("en(gas) != len(cost")
    total = 0
    local_sum = 0

    # [0, last_impossible] station are all
    # NOT starting
    last_impossible = -1
    
    for i in range(0,len(gas)):
        left = gas[i] - cost[i]
        local_sum += left
        total += left
        if local_sum < 0:
            local_sum = 0
            last_impossible = i
            
    if total < 0: return -1
    else : return last_impossible + 1

def main():
    #TODO: test
    return
    
if __name__ == "__main__":
    main()
