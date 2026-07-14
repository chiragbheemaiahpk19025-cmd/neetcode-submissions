class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["+", "-", "*", "/"]
        st = []
        res = 0
        for token in tokens:
            print("Stack", st)
            if token not in op:
                st.append(int(token))
            else:
                n1 = int(st.pop())
                n2 = int(st.pop())
                if token == "+":
                    st.append(n1 + n2)
                elif token == "-":
                    st.append(n2 - n1)
                elif token == "*":
                    st.append(n1 * n2)
                else:
                    st.append(n2 / n1)
        return int(st[-1])