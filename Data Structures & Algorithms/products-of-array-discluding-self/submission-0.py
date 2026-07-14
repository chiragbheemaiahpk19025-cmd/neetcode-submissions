class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # have a prefix array
        # have a suffix array
        # prefix i - 1* suffix i +1

        prefix = [1]
        suffix = [1]

        for num in nums:
            prefix.append(prefix[-1] * num)
        print(prefix)

        nums.reverse()
        for num in nums:
            suffix.append(suffix[-1] * num)
        print(suffix)
        

        res = []
        i = 0
        while i < len(nums):
            res.append(prefix[i] * suffix[len(nums) - 1 - i])
            i += 1
        return res
    