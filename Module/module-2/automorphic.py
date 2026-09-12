def is_automorphic(x):
    sq = x**2
    l = len(str(x))
    if x== int(str(sq)[-l:]):
        return "AutoMorphic Number"
    else:
        return "Non AutoMorphic Number"