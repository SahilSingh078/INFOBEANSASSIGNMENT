a,b,c,d,e = map(int,input("Enter Your Five Subject Marks [with space]: ").split())
total = (a+b+c+d+e)
avrg = (total/5)
prcnt = (total/(500))*100

print("Total: {} Average: {} Percentage: {}  ".format(total,avrg,prcnt))