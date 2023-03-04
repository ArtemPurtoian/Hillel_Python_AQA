# Task 1

numbers_1 = [19, 2, 55, 73, 28, 10, 69]
numbers_2 = [15, 10, 2, 77, 85, 69, 55, 38]
numbers_3 = set(numbers_1).intersection(set(numbers_2))
print(sorted(numbers_3))
print()

# Task 2

students = {
    "John": 4,
    "Angelina": 6,
    "Jacob": 10,
    "Elizabeth": 12,
    "Michael": 15,
    "Steven": 21
    }

average = sum(students.values())/len(students)
print(average)
for student in students.keys():
    if students[student] > average:
        print(student)

# Task 3

integers_list = [2, -9, 0, 51, 4, 28, -123, 9, 4, 2, 62, 51, 0]
different_values_amount = len(set(integers_list))
print(f"\nThe amount of different values is {different_values_amount}.")

# Task 4

list_1 = list(map(int, input("\nEnter numbers for the 1st list, "
                             "separate by space: ").split(' ')))
list_2 = list(map(int, input("Enter numbers for the 2nd list, "
                             "separate by space: ").split(' ')))
list_3 = sorted(list(set(list_1).intersection(set(list_2))))

print("\n1st list numbers:")
for number in list_1:
    print(number, end=' ')

print("\n2nd list numbers:")
for number in list_2:
    print(number, end=' ')

print("\n3rd list numbers:")
for number in list_3:
    print(number, end=' ')
print()
print()

# Task 5

data = "one two three one four five seven ten seven one"
split_data = data.split()
data_in_dict = {}

for el in split_data:
    data_in_dict[el] = data.count(el)

for el in data_in_dict.items():
    print(el, end=' ')
