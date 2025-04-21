def backspaceCompare(s: str, t: str) -> bool:
    i, j = len(s) -1, len(t) - 1 
    count_s, count_t = 0, 0
    while True:
        while i>=0:
            if s[i] == "#":
                count_s += 1
                i -=1
            elif s[i] != "#" and count_s:
                count_s -=1 
                i -= 1
            else:
                break 
        while j>=0:
            if t[j] == "#":
                count_t += 1
                j -= 1
            elif t[j] != "#" and count_t:
                count_t -=1 
                j -= 1
            else:
                break 
        if i<0 and j<0:
            return True 
        if i<0 or j<0:
            return False 
        if s[i] != t[j]:
            return False 
        i -= 1
        j -= 1
    
                
                
                

                
print(backspaceCompare("bxj##tw", "bxj###tw"))        






