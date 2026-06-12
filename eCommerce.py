print("Welcome to NIWA's Online Store")

#get user input for username and password
username = input("Enter Username: ")
password = input("Enter Password: ")

#role-based login
role = ""
if username == "admin" and password == "admin123":
    role = "admin"
    print("Login Successful. Welcome Admin")

elif username == "customer" and password == "cust123":
    role = "customer"
    print("Login Successful. Welcome Customer")

elif username == "cashier" and password == "cash123":
    role = "cashier"
    print("Login Successful. Welcome Cashier")

else:
    print("Invalid username or password.")
    exit()

#role-based access control
customers = ["customer"]
cashiers = ["cashier"]

if role == "admin":
    print("\n--- ADMIN PANEL ---")
    print("1. Checkout")
    print("2. View Reports")
    print("3. Manage Users")

    print("\nRegistered Customers:")
    for customer in customers:
        print(customer)

    print("\nRegistered Cashiers:")
    for cashier in cashiers:
        print(cashier)

elif role == "customer":
    print("1. Checkout")

elif role == "cashier":
    print("1. Process Sale")

#get user input for subtotal, coupon code, and location
subtotal = float(input("Enter Total Purchase Amount: "))
coupon = input("Enter coupon code: ").upper()
location = input("Enter Location: ").lower()

#calculate discount based on subtotal
if subtotal >= 200000:
    discount_rate = 0.15
elif subtotal >= 100000:
    discount_rate = 0.10
elif subtotal >= 50000:
    discount_rate = 0.05
else:
    discount_rate = 0
discount = subtotal * discount_rate

#calculate tax based on location
if location == "kampala":
    tax_rate = 0.18
elif location == "jinja":
    tax_rate = 0.15
elif location == "mbarara":
    tax_rate = 0.12
else:
    tax_rate = 0.10

tax = subtotal * tax_rate
print(f"Tax for {location.capitalize()}: {tax:.2f}")

#coupon code validation
coupon_discount = 0
if coupon == "SAVE10":
    coupon_discount = subtotal * 0.10
    print("Coupon applied successfully. You saved 10% on your purchase.")

elif coupon == "SAVE20":
    coupon_discount = subtotal * 0.20
    print("Coupon applied successfully. You saved 20% on your purchase.")

else:
    coupon_discount = 0
    print("Invalid coupon")

#calculate subtotal after discounts
final_price = subtotal - discount - coupon_discount + tax
print(f"Final Price: {final_price:.2f}")

#Generate receipt
print("\n--- RECEIPT ---")
print(f"User: {username}")
print(f"Role: {role}")
print(f"Location: {location}")
print(f"Subtotal: UGX {subtotal:,.2f}")
print(f"Tier Discount: UGX {discount:,.2f}")
print(f"Coupon Discount: UGX {coupon_discount:,.2f}")
print(f"Tax: UGX {tax:,.2f}")
print(f"Final Amount: UGX {final_price:,.2f}")