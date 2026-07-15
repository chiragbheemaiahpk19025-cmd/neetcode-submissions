class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)

        # the idea is check for elements where 1 less than number is not present, only then check forward

        for num in nums:
            hash_map[num] += 1

        maxi = 0
        for num in nums:
        
            if hash_map.get(num-1) == None:
                # means it is the first number in the sequence
                length = 1
                curr_num = num
                while hash_map.get(curr_num + 1) != None:
                    length += 1
                    curr_num += 1
                maxi = max(maxi, length)

        return maxi
