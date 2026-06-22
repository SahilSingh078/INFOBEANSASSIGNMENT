a,b,c,d,e,f = map(int,input("Enter value of 6 units [with space]: ").split())

if a >= b:
    if a >= c:
        if a >= d:
            if a >= e:
                if a >= f:
                    max_val = a
                else:
                    max_val = f
            else:
                if e >= f:
                    max_val = e
                else:
                    max_val = f
        else:
            if d >= e:
                if d >= f:
                    max_val = d
                else:
                    max_val = f
            else:
                if e >= f:
                    max_val = e
                else:
                    max_val = f
    else:
        if c >= d:
            if c >= e:
                if c >= f:
                    max_val = c
                else:
                    max_val = f
            else:
                if e >= f:
                    max_val = e
                else:
                    max_val = f
        else:
            if d >= e:
                if d >= f:
                    max_val = d
                else:
                    max_val = f
            else:
                if e >= f:
                    max_val = e
                else:
                    max_val = f
else:
    if b >= c:
        if b >= d:
            if b >= e:
                if b >= f:
                    max_val = b
                else:
                    max_val = f
            else:
                if e >= f:
                    max_val = e
                else:
                    max_val = f
        else:
            if d >= e:
                if d >= f:
                    max_val = d
                else:
                    max_val = f
            else:
                if e >= f:
                    max_val = e
                else:
                    max_val = f
    else:
        if c >= d:
            if c >= e:
                if c >= f:
                    max_val = c
                else:
                    max_val = f
            else:
                if e >= f:
                    max_val = e
                else:
                    max_val = f
        else:
            if d >= e:
                if d >= f:
                    max_val = d
                else:
                    max_val = f
            else:
                if e >= f:
                    max_val = e
                else:
                    max_val = f

print("Highest Stock =", max_val)