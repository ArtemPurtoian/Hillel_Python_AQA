import math


# Task 1
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
full_name = first_name + " " + last_name
print(f"Your full name is {full_name}.")

print(f"\nYour full name is {full_name}.".lower())
print(f"Your full name is {full_name}.".upper())
print(f"Your full name is {full_name}.".title())

print(f"\nYour full name is {full_name}." * 5)

full_name = f"\n\t{first_name} {last_name}\n"
print(f"\nThis is your full name with tab and new lines - {full_name}...")
print(f"This is your full name with rstrip - {full_name.rstrip()}...")
print(f"This is your full name with lstrip - {full_name.lstrip()}...")
print(f"This is your full name with strip - {full_name.strip()}...")

full_name = full_name.strip()
print(f"\nThis is your full name - {full_name}...")

# Task 2
radius = input("\nWhat is the radius of the circle?\n")
radius = int(radius)
circle_length = 2 * math.pi * radius
circle_area = math.pi * radius**2
print(f"The circle length is {round(circle_length, 2)}.")
print(f"The circle area is {round(circle_area)}.")

# Task 3
dollar_to_hryvnia = input("\nWhat is the current dollar to hryvnia rate?\n")
dollar_to_hryvnia = float(dollar_to_hryvnia)
hryvnia = 1 / dollar_to_hryvnia
hryvnia = round(hryvnia, 2)
print(f"\nThe current hryvnia to dollar rate is: {hryvnia}")
