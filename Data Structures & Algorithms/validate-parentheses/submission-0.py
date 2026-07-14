class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if (c == "(") or (c == "{") or (c == "["):
                
                st.append(c)
            else:
                if st:
                    if (st[-1] == "(" and c != ")") or (st[-1] == "{" and c != "}") or (st[-1] == "[" and c != "]"):
                        return False
                    else:
                        st.pop()
                else:
                    return False
        return len(st) == 0
                    
        