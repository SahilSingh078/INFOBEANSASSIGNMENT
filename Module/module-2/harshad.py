def is_harshad(x):
    sum =0
    for i in str(x):
        sum+=int(i)
    if x%sum==0:
        return "Harshad Number"
    else:
        return "Non Harshad Number"