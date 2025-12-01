print("Task67")#Task 67
def coordinator(x, y):
    my_tuple = (x, y)
    return my_tuple
my_coordinates = coordinator(5, 6)
print(my_coordinates)


print("")
print("Task68")#Task68

my_coordinates = {}
def coordinator(x,y): #function here
    mytuple = (x,y)
    return mytuple
my_coordinates[coordinator(0,0)] = "Home"
my_coordinates[coordinator(1,1)] = "Work"
my_coordinates[coordinator(-1,-1)] = "School"

for k,v in my_coordinates.items():
    print(f"position: {k} name: {v}")

print("")
print("Task69")#Task69


def best_weapon(weapon_list: list):
    
    best_value = 0
    best_weapon = ""
    for k,v in weapon_list:
        if v > best_value:
            best_weapon = k
    print(best_weapon)
weapon1 = ("blade", 10)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)
meele_weapon = [weapon1, weapon2, weapon3]
best_weapon(meele_weapon)


print("")
print("Task70")#Task70
 
game_table = [["_","_","_"],["_","_","_"],["_","_","_"]]
user_inputs = [0, 0]
state = True
count = 0
while state:
    if(count >= 2):
        usr_inp2 = input("Please type new or exit: ")        
        if str.lower(usr_inp2) == "exit":
            state = False
        elif str.lower(usr_inp2) == "new":
            count = 0
    elif(count == 0):
        user_inputs[0] = int(input("please enter x: "))
    elif(count == 1):
        user_inputs[1] = int(input("please enter y: "))
    count = count + 1

#Your code here
game_table[user_inputs[0]][user_inputs[1]] = "*"
print(f"{game_table[0][0]} {game_table[1][0]} {game_table[2][0]}")
print(f"{game_table[0][1]} {game_table[1][1]} {game_table[2][1]}")
print(f"{game_table[0][2]} {game_table[1][2]} {game_table[2][2]}")


print("")
print("Task 71 and 72")#Task71&72

my_set = set() 
state2 = True

while state2:
    usr_inp3 = input("Enter an element for set: ")
    if(str.lower(usr_inp3) == "exit"):
        state2 = False
    else:
        if(usr_inp3 in my_set):
            print("Please enter an unique element")
        else:
            my_set.add(usr_inp3)

for i in my_set:
    print(i)


print("Task75")#Task75

def start_game():
 print(f"Game started! Current score: 10")
 return 10

def increase_score(_score, value):
 _score += value
 print(f"Score increased! Current score: {_score}")
 return _score

def display_score(_score):
 print(f"Final score: {_score}")

score = 0
score = start_game()
score = increase_score(score, 5)
display_score(score)