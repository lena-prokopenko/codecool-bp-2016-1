amount = int(input("enter the current balance: "))

#if the amount is less than zero(negative) apply $10 fee
if amount < 0:
  amount = amount - 10

#if the amount is zero, apply a $5 fee
elif amount == 0:
  amount = amount - 5

#if the amount is up to $500, apply a $1 fee
elif ( amount > 0 and amount < 500 ):
  amount = amount - 1

#if the amount is exactly 500 bucks, then don't do anything
elif amount == 500:
    pass

#if amount amount is greater than 500 but less than 1000, add 1%
elif amount > 500 and amount < 1000:
  amount = amount + (amount / 100)

#and finally if amount is over 1000, the client gets 2%
elif amount >= 1000:
  amount = amount + (amount / 100) * 2
else:
    print("Amount out of range")

print("your final balance is: ")
print(amount)
