class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = defaultdict(list)
        res = []
        for s in strs:
            sorted_s = sorted(s)
            sorted_str_s = "".join(sorted_s)
            grouping[sorted_str_s].append(s)

        for v in grouping.values():
            res.append(v)
        return res