def greet():
    print("Welcome to the art supplies store!")
    print("How may we help you?")
greet()

items = int(input("Enter no. of item(s) bought: "))
for i in range(items):
    price_per_item = float(input("Enter the price of the supplies: "))
    x = price_per_item
    x = price_per_item

def calc_total(price_per_item, items):
    total = float(price_per_item * items)
    return total

total = calc_total(price_per_item, items)
r_total = round(total, 2)

amount_paid = float(input("How much did you pay? "))
def calc_change(paid, total):
    change = paid - total
    return change
change = calc_change(amount_paid, total)

def thanks(items):
    if items > 4:
        print("WOW That's a big order!! Thank you so so much for shopping with us!")
    else:
        print("Thanks a lot for shopping with us. Hope you come again")

closing = thanks(items)
print("\n======== ART SUPPLY RECEIPT ========")
print("Price per supply: ", price_per_item)
print("No. Items sold: ", items)
print("Amount Paid: ", amount_paid)
print('Change Due: ', change)
print('Rounded Total Cost: ', r_total)
print(closing)
print('===========================================\n')