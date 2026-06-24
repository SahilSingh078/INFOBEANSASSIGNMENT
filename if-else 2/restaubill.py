a  = int(input("Enter Your Bill Amount: " ))
if a <=1000:
    gst = a*0.05
    bill = a + gst
elif 1001<=a<=5000:
    gst = a * 0.12
    bill = a + gst
else: 
    gst = a * 0.18
    bill = a + gst

print("Final Bill Amount: ", bill)
