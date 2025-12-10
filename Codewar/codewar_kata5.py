def longest(a1, a2):
    string = []
    for i in a1:
        if i not in string:
            string.append(i)
    for j in a2:
        if j not in string:
            string.append(j)
                    
    string.sort()        
    return "".join(string)
    
    
a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"    
print(longest(a1, a2))