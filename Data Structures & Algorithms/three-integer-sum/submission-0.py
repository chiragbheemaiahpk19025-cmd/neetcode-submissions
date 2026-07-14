class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        hashmap = defaultdict(int)

        for i, num in enumerate(nums):
            hashmap[num] = i
        print(hashmap)
        
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                curr_sum = nums[i] + nums[j]
                print(curr_sum)
                target = hashmap.get((curr_sum * -1), None)
                if target != None and target > i and target > j:
                    temp_res = tuple(sorted([nums[i], nums[j], curr_sum * -1]))
                    res.add(temp_res)
                    print(res)
        sol = []
        for item in res:
            sol.append(list(item))
        return sol