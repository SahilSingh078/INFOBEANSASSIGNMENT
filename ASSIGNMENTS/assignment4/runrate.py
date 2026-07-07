a= float(input("Enter Over : "))
totalruns =int(input("Enter Total runs: "))
totalovers = (a*10)//10
remballs = (a*10)%10
leftballs = remballs/6
actualover = totalovers + leftballs
totalballs = (totalovers*6) + remballs
runrate = totalruns/actualover
	
print("Total balls: ", totalballs, "Run rate: ",runrate)