#for my second Python project I will make a Tip Calculator

# 1. Create an opening message
print('Welcome to The Tip Calculator!') 

# 2. Find what the total bill was? (I'll be using dollars as we don't usually tip where I live)
bill = input('What was the total bill? $')

# 3. What percenage tip would the user like to give? 10, 12 or 15?
percentage_tip = input('What percentage tip would you like to give? 10, 12 or 15? ')

tip = int(percentage_tip) / 100
new_tip = float(bill) * tip
total_bill = float(bill) + new_tip

# 4. How many people are splitting the bill
bill_split = input('How many people are splitting the bill? ')
split_bill = total_bill / int(bill_split)
result = round(split_bill, 2)
print(f'You should each pay ${result}')