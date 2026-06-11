#  Python compound interest calculator

principle = 0
rate = 0
time = 0

while True < 0:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be negative. Please try again.")
    else:
        break

while True <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("rate can't be 0 or negative. Please try again.")
    else:
        break

while True <= 0:
    time = float(input("Enter the time: "))
    if time <= 0:
        print("Time can't be 0 or negative. Please try again.")
    else:
        break


# Calculate compound interest
print(principle)
print(rate)
print(time)
amount = principle * (1 + rate / 100) ** time
print(amount)

print(f"Balance after {time} years: ₹{amount:.2f}")