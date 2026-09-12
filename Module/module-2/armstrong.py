def is_armstrong(x):
    digit = len(str(x))
    sum = 0
    for i in str(x):
        sum+= int(i)**digit
    if sum == x:
        return "Armstrong Number"
    else:
        return "Non Armstrong Number"