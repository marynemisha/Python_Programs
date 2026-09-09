#Write a program to group a list of strings into anagram groups.
words = ["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "live"]
groups = []
for word in words:
    placed = False
    for group in groups:
        count1 = {}
        for ch in word:
            if ch in count1:
                count1[ch] += 1
            else:
                count1[ch] = 1
        count2 = {}
        for ch in group[0]:
            if ch in count2:
                count2[ch] += 1
            else:
                count2[ch] = 1
        if count1 == count2:
            group.append(word)
            placed = True
            break
    if not placed:
        groups.append([word])
for g in groups:
    print(g)
