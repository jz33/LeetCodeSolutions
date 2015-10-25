class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.ctr = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.ctr:
            self.ctr[number] += 1
        else:
            self.ctr[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        ctr = self.ctr # speeds up
        for num in ctr:
            if value - num in ctr and (value - num != num or ctr[num] > 1):
                return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
