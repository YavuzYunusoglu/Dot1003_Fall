state = True
mylist = []
while state:
    game = input("Enter a game: ")
    if(str.lower(game) == "exit"):
        state = False
    else:
        mylist.append(game)

print(mylist)

def anarya(game_list):
    reverse_list = []
    for i in range(len(game_list), 0, -1):
        reverse_list.append(game_list[i - 1])
    return reverse_list
        
mylist = anarya(mylist)
print(mylist)