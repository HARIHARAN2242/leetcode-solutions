class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        longest = 0

        for num in numset:
            if num - 1 not in numset:      # Start of a sequence
                count = 1
                current = num

                while current + 1 in numset:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest