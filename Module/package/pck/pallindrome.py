def is_pall(x):
    if str(x)==str(x)[::-1]:
        return "Pallindrome Number"
    else:
        return "Not Pallindrome Number"