def listt(number):
    empty_list = []

    for element in range(0, number):
        empty_list.insert(0, element)
     
    return empty_list

number_to_insert = int(input("How many elements do u wanna to appear on list: "))
print(listt(number_to_insert))
print("See u later ;)")