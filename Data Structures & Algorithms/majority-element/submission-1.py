class Solution:
    # O(n) time | O(n) space
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority_element, max_frequency = 0, 0
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
            if count[nums[i]] > max_frequency:
                max_frequency = count[nums[i]]
                majority_element = nums[i]
        return majority_element