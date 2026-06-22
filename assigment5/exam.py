a,b = map(int,input("Enter your Marks and attendance [with space] ").split())
if a>=40:
    print("pass" )
    if b>=75:
      print("Eligible for certificate")
    else:
      print("NOT ELIGIBLE FOR CERTIFICATE")
else:
   print("try again!!!") 