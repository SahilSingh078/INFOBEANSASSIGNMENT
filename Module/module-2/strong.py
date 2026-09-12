def is_strong(x):
    total = 0
    for ch in str(x):
        d = int(ch)
        fact = 1
        for j in range(1, d + 1):
            fact *= j
        total += fact
    if total==x:
        return "Strong Number"
    else:
        return "Not Strong Number"