# Python weight convertor(Pounds to Kilograms)

weight = float(input("Enter your weight: "))
unit = input("Is the weight in Kilograms or Pounds? (K/L): ")

if unit =="K":
    wight = weight * 2.205
    unit = "lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
else:
    print(f"{unit}was not valid.")
    
print(f"Your weight is {round(weight, 1)} {unit}.")