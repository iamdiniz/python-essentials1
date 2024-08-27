numbers = [1, 2, 3]

total = 0

print("List: ", numbers)

for i in range(len(numbers)):
    total += numbers[i]
    # Somando cada valor no for

print("making a sum of all the values on the list: ", total)

# you can do that to:

# for i in numbers:
#     total += i

# doesn't need 'len()'
