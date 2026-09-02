'''
3.
ONLINE SHOPPING SYSTEM

Scenario:

An e-commerce company wants to develop an Online Shopping System.
 The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU
1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit

Requirements

Choice 1 – Customer Registration

* Accept Customer Name, Email, and Mobile Number.
* Pass the values to a function using Positional Arguments.
* Display the registered customer details.

Choice 2 – Product Information

* Accept Product Name, Price, and Category.
* Call the function using Keyword Arguments.
* Display the product details.

Choice 3 – Generate Invoice

* Accept Product Name and Price.
* Tax Percentage should have a default value.
* Use Default Arguments while generating the invoice.
* Display the final amount.

Choice 4 – Add Multiple Products

* Allow the user to enter any number of product prices.
* Pass all prices to a function using Variable Length Arguments (*args).
* Calculate and display the total bill amount.

Choice 5 – Display Customer Profile

* Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
* Pass the details using Arbitrary Keyword Arguments (**kwargs).
* Display all customer information.

Choice 6 – Exit

Sample Execution

Enter Choice : 1

Enter Name : Ajay
Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
Enter Mobile : 9876543210

Customer Registered Successfully

---

Enter Choice : 2

Enter Product Name : Laptop
Enter Price : 55000
Enter Category : Electronics

Product Details Displayed Successfully

---

Enter Choice : 3

Enter Product Name : Laptop
Enter Price : 55000

Invoice Generated Successfully

---

Enter Choice : 4

Enter Number of Products : 4

Enter Price 1 : 100
Enter Price 2 : 200
Enter Price 3 : 300
Enter Price 4 : 400

Total Bill Amount : 1000

---

Enter Choice : 5

Customer Profile Displayed Successfully

---

Enter Choice : 6

Thank You. Program Terminated.

Important Instructions

1. Choice 1 must use Positional Arguments.
2. Choice 2 must use Keyword Arguments.
3. Choice 3 must use Default Arguments.
4. Choice 4 must use Variable Length Arguments (*args).
5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
6. Use separate functions for each menu option.
7. Implement the solution using a menu-driven approach.
8. Maintain proper code readability and formatting.

Note:
Marks will be awarded based on the correct usage of the specified argument type in each menu option.
'''
def registration(name,email,mobile):
    return name,email,mobile

def product(prod_name, prod_price, prod_category):
    return prod_name,prod_price,prod_category

def invoice(prod_name, prod_price, tax = 10):
    tax_amount = prod_price * (tax/100)
    final_amount = prod_price +tax_amount
    return prod_name,prod_price, final_amount

def multiple(*args):
    total = 0
    for i in args:
        total+=i
    return total

def customer(**kwargs):
    for k,v in kwargs.items():
        print(k, ":", v)

while True:
    print("\n******** ONLINE SHOPPING SYSTEM ********")
    print("1. Customer Registration")
    print("2. Product Information")
    print("3. Generate Invoice")
    print("4. Add Multiple Products")
    print("5. Display Customer Profile")
    print("6. Exit")
    choice = int(input("\nEnter Choice : "))
    match choice:
        case 1:
            name = input("PLEASE ENTER YOUR NAME: ")
            email = input("PLEASE ENTER YOUR EMAIL: ")
            mobile = int(input("PLEASE ENTER YOUR 10 Digit Phone Number: "))
            name, email, mobile = registration(name, email, mobile)
            print("Customer Registered Successfully")
            print("Name         :", name)
            print("Email        :", email)  
            print("Phone Number :", mobile)
        case 2:
            name  = input("Print Product Name: ")
            price = int(input("Enter Product Price: "))
            category = input("Enter category : ")
            name, price,category = product(prod_name = name, prod_price = price, prod_category = category)
            print("PRODUCT DETAILS")
            print("Product Name     : ", name)
            print("Product Price    : ",price)
            print("Product Category : ", category)
        case 3:
            name = input("Enter product name: ")
            price = int(input("Enter product price: "))
            name, price,finalamount = invoice(prod_name = name, prod_price = price)
            print("Product name: ", name)
            print("Product Price: ", price)
            print("Final Amount: ", finalamount)
        case 4:
            n = int(input("Enter no. of products: "))
            prices = []
            for i in range(1,n+1):
                price= int(input(f"Enter price of {i}: "))
                prices.append(price)
            bill = multiple(*prices)
            print("Total Bill: ", bill)
        case 5:
                name = input(f"Enter Name of {i+1}: ")
                city = input(f"enter city of {i+1}: ")
                email = input(f"Enter email of {i+1}: ")
                mobile = int(input(f"Enter Phone No. of {i+1}: "))
                print("\nCustomer Details ")
                customer(customer_name = name, customer_city = city, customer_email =email, customer_mobile = mobile)
        case 6:
            print("PROGRAM TERMINATED")
            break
        case _:
            print("Please Choose Valid Option")