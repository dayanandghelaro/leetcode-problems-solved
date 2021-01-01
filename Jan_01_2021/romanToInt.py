def romanToInt(self, s: str) -> int:
    romanNums = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
                'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if s in romanNums.keys():
        return romanNums[s]
    else:
        num = int(romanNums[s[0]])
        length = len(s)
        for i in range(1,length):
            num += romanNums[s[i]]
            if romanNums[s[i]] > romanNums[s[i-1]]:
                num -= romanNums[s[i-1]]
                num -= romanNums[s[i-1]]
        return num