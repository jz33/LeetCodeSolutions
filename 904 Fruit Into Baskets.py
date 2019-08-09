from typing import List

def totalFruit(tree: List[int]) -> int:
    baskets = {} # apple type : count
    lastOne = 0 # type of last apple
    continousCount = 0 # continous count of last apple
    maxAppleCount = 0 # result

    for apple in tree:
        if apple in baskets:
            # Apple already existed, check with last one
            # This condition must be first, consider [1,1]
            if apple == lastOne:
                continousCount += 1
            else:
                continousCount = 1
            baskets[apple] += 1

        elif len(baskets) < 2:
            # Baskests are not filled yet
            continousCount = 1
            baskets[apple] = 1

        else:
            # The 3rd type apple. Clear baskets except last one
            baskets = {}
            baskets[lastOne] = continousCount

            continousCount = 1
            baskets[apple] = 1

        lastOne = apple
        maxAppleCount = max(maxAppleCount, sum(baskets.values()))

    return maxAppleCount
                
