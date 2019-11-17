'''
774. Minimize Max Distance to Gas Station
https://leetcode.com/problems/minimize-max-distance-to-gas-station/

On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1],
where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

Example:

Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Note:

stations.length will be an integer in range [10, 2000].
stations[i] will be an integer in range [0, 10^8].
K will be an integer in range [1, 10^6].
Answers within 10^-6 of the true value will be accepted as correct.
'''
episilon = 10 ** (-6)

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        '''
        Use idea from 875 Koko Eating Bananas
        '''
        histo = collections.Counter()
        for i in range(1, len(stations)):
            dist = stations[i] - stations[i-1]
            histo[dist] += 1

        # left is minimum possible distance
        # right is maximum possible distance
        right = float(max(histo.items(), key = lambda x : x[0])[0])
        left = right / (K + 1)

        res = right
        while left <= right:
            mid = left + (right - left) / 2.0
            
            # Count total cut needed if every distance is less or equal to mid
            cuts = 0
            for dist,ctr in histo.items():
                t = dist / mid
                if math.isclose(t, int(t)):
                    cuts += ctr * (int(t) - 1)
                else:
                    cuts += ctr * (int(t))

            if cuts <= K:          
                res = mid
                right = mid - episilon
            else:
                left = mid + episilon

        return res
