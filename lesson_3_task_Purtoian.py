import random


# Task 1

min = random.randint(0, 59)

if min == 1:
    print(f"{min} minute. It's the 1st quarter.")
elif min == 0 and min <= 15:
    print(f"{min} minutes. It's the 1st quarter.")
elif min <= 30:
    print(f"{min} minutes. It's the 2nd quarter.")
elif min <= 45:
    print(f"{min} minutes. It's the 3rd quarter.")
else:
    print(f"{min} minutes. It's the 4th quarter.")

# Task 2

birth_month = input("\nEnter the month of your birth: ")
year_months = list(range(1, 13))
winter_months = [1, 2, 12]
spring_months = [3, 4, 5]
summer_months = [6, 7, 8]
autumn_months = [9, 10, 11]

try:
    if int(birth_month) in winter_months:
        print("Winter - snow was falling outside.")
    elif int(birth_month) in spring_months:
        print("Spring - everything around was blooming.")
    elif int(birth_month) in summer_months:
        print("Summer - children were enjoying their summer holidays.")
    elif int(birth_month) in autumn_months:
        print("Autumn - everything around had bright colors.")
    elif int(birth_month) not in year_months:
        print("A number of month is 1 to 12.")
except ValueError:
    print("This is not a number of month.")

# Task 3

number = random.randint(0, 999)
message_div = f"\n{number} is divisible by 6. You get {number/6}."
message_not_div = f"\n{number} is NOT divisible by 6."

if len(str(number)) == 3:
    digit_1 = number // 100
    digit_2 = number // 10 % 10
    digit_3 = number % 10
    total = digit_1 + digit_2 + digit_3

    if digit_3 in [0, 2, 4, 6, 8] and total % 3 == 0:
        print(message_div)
    else:
        print(message_not_div)

elif len(str(number)) == 2:
    digit_1 = number // 10
    digit_2 = number % 10
    total = digit_1 + digit_2

    if digit_2 in [0, 2, 4, 6, 8] and total % 3 == 0:
        print(message_div)
    else:
        print(message_not_div)

elif len(str(number)) == 1:
    if number in [0, 6]:
        print(message_div)
    else:
        print(message_not_div)

# Task 4

coordinate_x = float(input("\nWhat is the X coordinate? "))
coordinate_y = float(input("What is the Y coordinate? "))

if coordinate_x > 0 and coordinate_y > 0:
    print("\nThe point is in the I quarter.")
elif coordinate_x < 0 < coordinate_y:
    print("\nThe point is in the II quarter.")
elif coordinate_x < 0 and coordinate_y < 0:
    print("\nThe point is in the III quarter.")
elif coordinate_x > 0 > coordinate_y:
    print("\nThe point is in the IV quarter.")
elif coordinate_x > 0 or coordinate_x < 0 and coordinate_y == 0:
    print("\nThe point is on the X axis.")
elif coordinate_x == 0 and coordinate_y > 0 or coordinate_y < 0:
    print("\nThe point is on the Y axis.")
elif coordinate_x == 0 and coordinate_y == 0:
    print("\nThe point is at the origin.")
