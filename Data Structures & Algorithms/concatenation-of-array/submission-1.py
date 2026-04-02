class Solution:
    # O(n) time | O(n) space - where n is the length of the input array
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans 