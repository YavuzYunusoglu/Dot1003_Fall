#Assignment-3
"""

print("task54")#task54

text = "The quick brown fox jumps over the lazy dog"
usr_inpt = input("Wich item do you want to search: ")
print(f"item {usr_inpt} appeared {text.count(str.lower(usr_inpt))} times")


print("task55")#task55

search_text = input("Enter the input to search: ")
search_item = input("Which item do you want to search: ")
print(f"item {search_item} appeared {search_text.count(str.lower(search_item))} times")


print("task56")#task56

vowels = ["a", "e", "i", "o", "u"]

def clear_vowels(text1):
    for i in vowels:
        text1 = text1.replace(i, '')
    
    return text1

menu_button = "new game"
print(clear_vowels(menu_button))

#Assignment4


print("Task59")#Task59
mylist = ["Doom", "Max Payne", "FTL"]
print(mylist)
print(max(mylist, key=len))


print("Task60")#Task60


#create your function below:
x = 0
y = 0
finded = False
def finder(list_arg, element_arg):
    state = False
    for row in range(len(list_arg)):
      for colmn in range(len(list_arg[row])):
        if(list_arg[row][colmn] == element_arg):
            print(f"find at row: {row} column: {colmn}")
            state = True
    print(state)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
element = int(input("item to search: "))
print(finder(my_matrix, element))


print("Task61")#Task61

def sum_of_row(list_arg, element_arg):
    sum = 0
    for colmn in list_arg[element_arg]:
        sum = sum + colmn
    return sum
  
my_matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
element1 = int(input("row no: "))
print(sum_of_row(my_matrix1, element1))


print("Task62")#Task62

def sum_of_column(list_arg, element_arg):
    sum = 0
    for row in range(len(list_arg)):
        for colmn in range(len(list_arg[row])):
            if(colmn == element_arg):
                sum = sum + list_arg[row][colmn]
    return sum

my_matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
element2 = int(input("column no: "))
print(sum_of_column(my_matrix2, element2))


print("Task63")#Task63

def tripler(list_arg):
    new_list = list_arg[:]
    for i in range(len(new_list)):
        new_list[i] = new_list[i] * 3
    return new_list

my_lucky_numbers = [4,8,15,16,23,42]
tripled_numbers = tripler(my_lucky_numbers)
print(f"My Lucky Numbers: {my_lucky_numbers}")
print(f"Tripled Numbers: {tripled_numbers}")
"""

print("Task64")#Task64

inventory = {
"item1": 3,
"item2": 1,
"item3": 5
}

for key in inventory:
    print(f"{key}: {inventory[key]}")
print("Task65")#Task65


def add_item(item, quantity):
    if(inventory.__contains__(item)):
        inventory[item] = inventory[item] + quantity
    else:
        inventory[item] = quantity
        

def remove_item(item, quantity):
    if(inventory.__contains__(item)):
        if (inventory[item] - quantity) > 0:
            inventory[item] = inventory[item] - quantity
        else:
            inventory.pop(item)
    else:
        inventory.pop(item)

add_item("item1", 5)
add_item("item4", 1)

remove_item("item4", 6)
remove_item("item1", 2)

for key in inventory:
    print(f"{key}: {inventory[key]}")

