'''
93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits,
return all possible valid IP addresses that can be formed by inserting dots into s.
You are not allowed to reorder or remove any digits in s.
You may return the valid IP addresses in any order.

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
    1 <= s.length <= 20
    s consists of digits only.
'''
from functools import cache

def isValidSection(section: str) -> bool:
    '''
    Check if a section of the ip address is valid
    '''
    val = int(section)
    if val < 0 or val > 255:
        return False
    if len(section) > 1 and section[0] == '0':
        return False
    return True

class Solution:
    '''
    Real Tiktok interview question 20240304
    '''
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(input) < 4 or len(input) > 12:
            return []

        @cache
        def topDown(source: str, remainSectionCount: int) -> List[str]:
            '''
            @remainSectionCount: 4,3,2,1
            '''
            if not remainSectionCount <= len(source) <= remainSectionCount * 3:
                # invalid string size
                return []
            
            if remainSectionCount == 1:
                return [source] if isValidSection(source) else []
            else:
                result = []
                for right in range(1, 4):
                    if right <= len(source):
                        parent = source[:right]
                        if isValidSection(parent):
                            children = topDown(source[right:], remainSectionCount - 1)
                            for child in children:
                                result.append(parent + '.' + child)
                return result
        return topDown(s, 4)
