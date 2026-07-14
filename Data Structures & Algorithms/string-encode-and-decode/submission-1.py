class Solution:

    def encode(self, strs: List[str]) -> str:
        # We have an agreed upon scheme that should work for all inputs
        # all ascii characters possible
        # ;ength of the word can be more than a digit as well

        # PREAMBLE length of word PEAMBLE word

        symbol = "#"

        encoded_str = ""

        for s in strs:
            preamble = symbol + str(len(s)) + symbol
            substr = preamble + s
            encoded_str += substr

        print(encoded_str)
        return encoded_str
    
    
    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        symbol = "#"

        while i < len(s):
            j = i
            while j < len(s):
                if j != i and s[j] == symbol:
                    break
                j += 1
            length = int(s[i + 1: j])
            start = j + 1
            end = start + length
            # print(length)
            decoded_str.append(s[start: end])    
            # print(decoded_str)
            i = end
            # print(i)
            # break
        return decoded_str
