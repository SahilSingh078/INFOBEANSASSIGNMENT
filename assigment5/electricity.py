unit =int(input("Enter Consumed Unit: "))
if unit>=100:
    if unit>=300:
       print("Usage Category = High usage ")
    else:
       if unit>=200:
          print("usage category =Moderate usage ")
       else:
          print(" suage category = Normal usage ")
else:
    print("usage categry = LOW USAGE ")