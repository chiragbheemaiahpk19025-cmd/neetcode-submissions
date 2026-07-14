class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # nge
        res = []
        st = []
        for i in range(len(temperatures) - 1, -1, -1):
            print("Stack", st)
            if not st:
                st.append([temperatures[i], i])
                res.append(0)
            else:
                while st and st[-1][0] <= temperatures[i]:
                    st.pop()
                if not st:
                    res.append(0)
                else:
                    res.append(st[-1][1] - i)
                st.append([temperatures[i], i])
        res.reverse()
        return res