a,b =map(int,input("Enter Time in HRs and MiNs [with comma]: " ).split(","))
c = b/60
time = (a+c)
dist = 60*time
print("TOTAL TIME: ", time, "DISTANCE = ", dist,"km")