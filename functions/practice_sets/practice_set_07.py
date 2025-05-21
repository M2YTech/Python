def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["Muhammad", "Ahmed", "Sawaiba", "Amina", "na"]

print(rem(l, "na"))