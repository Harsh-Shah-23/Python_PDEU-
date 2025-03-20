# 5. Create two dictionaries – one containing grocery items and their prices 
# and another containing grocery items and quantity purchased. 
# By using the values from these two dictionaries compute the total bill.

prices = {'apple': 2, 'banana': 1, 'milk': 3}
quantity = {'apple': 4, 'banana': 6, 'milk': 2}

total_bill = sum(prices[item] * quantity[item] for item in prices if item in quantity)

print("Total Bill:", total_bill)
