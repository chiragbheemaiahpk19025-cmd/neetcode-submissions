class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)

        for i, num in enumerate(nums):
            hash_map[num] = i

        print(hash_map)
        res = [-1, -1]
        for i, num in enumerate(nums):
            diff = target - num
            if hash_map.get(diff, None) != None and i != hash_map[diff]:
                return [i, hash_map[diff]]
        return res
