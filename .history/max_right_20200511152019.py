def manacher(preS):
    s = '#' + '#'.join(preS) + '#'
    l = len(s)
    RL = [0] * l
    maxRight = pos = maxLen = 0
    for i in range(l):
        if i < maxRight:
            RL[i] = min(RL[2*pos - i], maxRight-i+1)
            if RL[i]==maxRight-i+1 and RL[i]!=RL[2*pos - i]:
                print("*",i,"RL[i]",RL[i])
        else:
            RL[i] = 1
        while i - RL[i] >= 0 and i + RL[i] < l and s[i - RL[i]] == s[i + RL[i]]:
            RL[i] += 1
        if i + RL[i] - 1 > maxRight:
            maxRight = i + RL[i] - 1
            pos = i
    maxLen = max(RL)
    idx = RL.index(maxLen)
    sub = s[idx - maxLen + 1: idx + maxLen]
    print(RL,end='')
    print()
    print(s,end='')
    print()
    return sub.replace('#', '')

if __name__ == "__main__":
    str="abababaababds"
    p=manacher(str)
    print(p)