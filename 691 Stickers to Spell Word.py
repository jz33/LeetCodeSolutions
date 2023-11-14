'''
691. Stickers to Spell Word
https://leetcode.com/problems/stickers-to-spell-word/

We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. 
You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

Example 1:

Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

Example 2:

Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.

Constraints:

    n == stickers.length
    1 <= n <= 50
    1 <= stickers[i].length <= 10
    1 <= target.length <= 15
    stickers[i] and target consist of lowercase English letters.

'''
from functools import cache
from typing import List, Tuple


def minStickers(stickers: List[str], target: str):
    # It is impossible to use more than target length # of stickers
    inf = len(target) + 1

    def getHisto(word: str) -> List[int]:
        histo = [0] * 26
        for char in word:
            histo[ord(char) - ord("a")] += 1
        return histo

    stickerHistos = list(map(lambda sticker: getHisto(sticker), stickers))
    targetHisto = getHisto(target)

    @cache
    def dfs(si: int, targetState: Tuple[int]) -> int:
        """
        @si: index in stickers
        @targetState: current matching state of target
        @return: # of stickers used
        """
        if sum(targetState) == 0:
            return 0
        if si >= len(stickers):
            return inf

        # If not using this sticker
        skipResult = dfs(si + 1, targetState)
        sticker = stickerHistos[si]

        # If there aren't no single match of target and sticker,
        # can only skip this sticker but only use s1
        for i in range(26):
            if sticker[i] and targetState[i]:
                break
        else:
            return skipResult

        # If using this sticker, try match as much as possible
        nextState = list(targetState)
        for i in range(26):
            nextState[i] = max(0, targetState[i] - sticker[i])

        useResult = 1 + dfs(si, tuple(nextState))
        return min(skipResult, useResult)

    ans = dfs(0, tuple(targetHisto))
    return -1 if ans == inf else ans


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        return minStickers(stickers, target)
