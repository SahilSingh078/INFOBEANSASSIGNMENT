a,b = map(int,input("Enter Your Total Bill Amount: and Number Of friends [with space]: ").split())

gst = 0.05*a
servicecharge = 0.1*a

final = (a+gst+servicecharge)
each = final/b

#print("Final Bill: ",final," AND Each PErson Pays: ", each)
#print(f"Final Bill : {final} Each Person Pays: {each}")
print("Final Bill: {} Each pays: {}".format(final,each))