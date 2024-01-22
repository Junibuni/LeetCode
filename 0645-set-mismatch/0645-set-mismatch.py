class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicated_num = sum(nums) - sum(set(nums))
        expected_sum = sum(range(1, len(nums)+1))
        return [duplicated_num, expected_sum - sum(set(nums))]