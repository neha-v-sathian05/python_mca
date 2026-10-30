import re

# Validate email address
email = input("Enter email address: ")
# Validate phone number
phone = input("Enter phone number: ")

if re.fullmatch(r"[6-9][0-9]{9}", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

# Extract transaction IDs from logs
log = input("Enter log message: ")

transaction_ids = re.findall(r"TXN[0-9]+", log)

if transaction_ids:
    print("Transaction IDs found:", transaction_ids)
else:
    print("No transaction IDs found")