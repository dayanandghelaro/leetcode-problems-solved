class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = s.replace('(','0')    # replace ( with zeros
        s = s.replace(')', '1')   # replace ) with ones
        s = s.replace('01', 'x')  # figure out where valid pair
        pattern = "0x1"           # look for nested pairs
        while True:
            while pattern not in s and len(pattern) < len(s):
                pattern = pattern[:-1]+"x"+"1"
            s = s.replace(pattern, 'x'*(pattern.count('x')+1))
            pattern = pattern[:-1]+"x"+"1"
            if len(pattern) >= len(s):
                break
        previousValidSequence = 0
        currentValidSequence = 0
        for c in s:
            if c == "x":
                currentValidSequence +=1
            else:
                if previousValidSequence < currentValidSequence:
                    previousValidSequence = currentValidSequence
                currentValidSequence = 0
        if previousValidSequence < currentValidSequence:
            previousValidSequence = currentValidSequence
        return previousValidSequence*2
