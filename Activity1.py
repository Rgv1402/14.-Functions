def greet_customer():
    print('Welcome to our lemonade stand!')
    print("Fresh lemonade, made just for you!")

greet_customer()

per_cup = float(input("Enter price of cup: "))
cups_sold = int(input("Enter no. of cups sold: "))
def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(per_cup, cups_sold)
rounded_total = round(total_cost, 2)
print("Total cost = ", rounded_total, " $")

amount_paid = float(input("Enter amount paid by customer: "))

def calc_change(paid, total):
    change = paid - total
    return change

change_due = calc_change(amount_paid, total_cost)
rounded_change = round(change_due, 2)

def thankyou_msg(cups):
    if cups > 5:
        return("WOW that's a big order! Thank you so much for your support")
    else:
        return("Thanks for stopping by the stand")

closing_msg = thankyou_msg(cups_sold)

print("\n======== LEMONADE STAND RECEIPT ========")
print("Price per cup: ", per_cup)
print("Cups sold: ", cups_sold)
print("Amount Paid: ", amount_paid)
print('Change Due: ', rounded_change)
print('Total Cost: ', rounded_total)
print(closing_msg)
print('===========================================\n')