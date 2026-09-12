def is_neon(x):
    sq = x**2
    sum = 0
    for i in str(sq):
        sum+=int(i)
    if x==sum:
        return "Neon Number"
    else:
        return "Non Neon Number"