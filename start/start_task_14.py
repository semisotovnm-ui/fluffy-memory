def max_sequence(n):
    if not n:
        return 0
    max_s = s = 0
    for i in n:
        s = max(0,s+i)
        max_s = max(max_s,s)
    return max_s
n = list(map(int,input().split()))
print(max_sequence(n))