def isValid(self, s: str) -> bool:
    startBrackets = []
    bol =False
    if len(s) <= 1:
        bol = False
    else:
        for c in s:
            if c in "{[(":
                startBrackets.append(c)
            elif c in "}])":
                if len(startBrackets) == 0:
                    bol=False
                    break
                toClose = startBrackets[-1]
                if (toClose=="(" and c ==')') or (toClose=="{" and c=="}") or (toClose=="[" and c=="]"):
                    del(startBrackets[-1])
                    bol=True
                else:
                    bol=False
                    break
    if len(startBrackets) > 0:
        bol=False
    return bol
