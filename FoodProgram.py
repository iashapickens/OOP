import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0

customer_data = {
    570: ["Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", False],
    569: ["Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", "ahimsworthfs@list-manage.com", "254-555-2273", True]
}

# Ask user for customer ID
cust_id = int(input("Enter Customer ID (570 or 569): "))

# Create Customer instance
cust_info = customer_data[cust_id]
customer = fc.Customer(cust_id, *cust_info)

# Create Transaction instances for this customer
customer_transactions = []
for t in dict.values():  # Use the existing 'dict'
    if t[3] == cust_id:  # Match customer ID
        customer_transactions.append(fc.Transaction(t[0], t[1], t[2], t[3]))

# Generate report
print("\n--- Customer Information ---")
print(f"Customer ID: {customer.get_customerid()}")
print(f"Name: {customer.get_name()}")
print(f"Address: {customer.get_address()}")
print(f"Email: {customer.get_email()}")
print(f"Phone: {customer.get_phone()}")
print(f"Member Status: {'Yes' if customer.get_member_status() else 'No'}")

print("\n--- Transactions ---")
order_total = 0
for trans in customer_transactions:
    print(f"{trans.get_date():10} | {trans.get_item_name():20} | ${trans.get_cost():.2f}")
    order_total += trans.get_cost()

# Apply discount if customer is a member
if customer.get_member_status():
    discount = order_total * 0.2
    order_total -= discount
    print(f"\nDiscount (20%): -${discount:.2f}")

print(f"Total Due: ${order_total:.2f}")


