"""
774. Minimize Max Distance to Gas Station
https://leetcode.com/problems/minimize-max-distance-to-gas-station/

You are given an integer array stations that represents the positions
of the gas stations on the x-axis. You are also given an integer k.

You should add k new gas stations.
You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

Return the smallest possible value of penalty().
Answers within 10-6 of the actual answer will be accepted.

Example 1:

Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
Output: 0.50000

Example 2:

Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
Output: 14.00000

Constraints:
    10 <= stations.length <= 2000
    0 <= stations[i] <= 108
    stations is sorted in a strictly increasing order.
    1 <= k <= 106
"""

epsilon = 10 ** (-6)


class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        """
        Use idea from 875 Koko Eating Bananas
        """
        histo = collections.Counter()
        for i in range(1, len(stations)):
            dist = stations[i] - stations[i - 1]
            histo[dist] += 1

        # left is minimum possible distance
        # right is maximum possible distance
        right = float(max(histo.items(), key=lambda x: x[0])[0])
        left = right / (K + 1)

        res = right
        while left <= right:
            mid = left + (right - left) / 2.0

            # Count total cut needed if every distance is less or equal to mid
            cuts = 0
            for dist, ctr in histo.items():
                t = dist / mid
                if math.isclose(t, int(t)):
                    cuts += ctr * (int(t) - 1)
                else:
                    cuts += ctr * (int(t))

            if cuts <= K:
                res = mid
                right = mid - epsilon
            else:
                left = mid + epsilon

        return res
