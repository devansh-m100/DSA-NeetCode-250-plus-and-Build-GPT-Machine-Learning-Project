class Solution:
    # O(1) time | O(1) space
    def hammingWeight(self, n: int) -> int:

        numOfOneBits = 0

        while n:
            n &= n - 1
            numOfOneBits += 1
        
        return numOfOneBits