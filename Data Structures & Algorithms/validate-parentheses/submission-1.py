class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in ["(", "{", "["]:
                st.append(c)
            elif not st or (c == ")" and st[-1] != "(") or (c == "}" and st[-1] != "{") or (c == "]" and st[-1] != "["):
                return False
            else:
                st.pop()
            print(st)
        return len(st) == 0
