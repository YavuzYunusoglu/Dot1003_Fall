tree_length = int(input("Spruce height: "))
box_size = int(input("Box Size: "))
if(tree_length > 0):
    check = 1
    for i in range(0, tree_length, 1):
        check = check + 2
    if(check <= box_size):
        print('-' * box_size)
        space_length = tree_length
        index = 1
        print(f"|{' ' * box_size}|")
        for i in range(0, tree_length, 1):
            print(f"|{' ' * space_length}{'*' * index}{' ' * (box_size - (space_length + index))}|")
            space_length = space_length - 1
            index = index + 2
        print(f"|{tree_length * ' '}*{' ' * (box_size - (1 + tree_length))}|")
        print('-' * box_size)
    else:
        print(f"Box size must be higher than {check} for {tree_length}.")
else:
    print("Please enter a positive number.")

