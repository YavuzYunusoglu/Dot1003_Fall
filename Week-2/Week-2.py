#Task11
fah = int(input("Please type in a temperature (f): "))
cel = (fah- 32) / 1.8
print(f"{fah} degrees Fahrenheit equals {cel} degrees Celsius!")
if(cel < 0):
    print("Brr, It's cold in here!")


print("")#Task12

hourly_wage = float(input("How much do you earn an hour: "))
hours_worked = int(input("How many hours do you work on a day: "))
wich_day = input("Wich day do you choose for calculate: ")
if(wich_day.lower() == "sunday"):
    price = hourly_wage * 2 * hours_worked
    print(f"Daily wages: {price}")
else:
    price = hourly_wage * hours_worked
    print(f"Daily wages: {price}")


print("")#Task13

age = int(input("How old are you? "))
if(age < 18):
    print("You can't play Dark Souls")
elif age > 18 and age < 44:
    print("You can play this game")
else:
    print("You are too old for this sh*t")


print("")#Task14

num1 = int(input("Type the first number: "))
num2 = int(input("Type the second one: "))
if (num1 > num2):
    print(f"First one is greater ({num1}>{num2})")
elif (num1 < num2):
    print(f"Second one is greater ({num1}<{num2})")
else:
    print(f"These are equal ({num1}={num2})")


print("")#Task15

game_1 = input("Type the first game: ")
game_2 = input("Type the second one: ")
if (game_1 > game_2):
    print(f"{game_2} comes aphabetically last")
elif (game_1 == game_2):
    print("These are same!")
else:
    print(f"{game_1} comes alphabetically last!")


print("")#Task16

def is_belong_fallout(inp):
    print(inp)
    comms = {
    "NCR", "Brotherhood of Steel", "Caesar's Legion", "Great Khans", "Vault Dweller"
    }
    if(inp in comms):
        return True
    
if(is_belong_fallout(input("Wich comm do you belong to?: "))):
    print("You're belong to Fallout Universe")
else:
    print("You're not belong to Fallout Lore")


print("")#Task17

results = int(input("What's your exam result: ")) 
if(results < 0):
    print( "You What?")
elif(results >= 0 and results < 50):
    print("Fail")
elif(results >= 50 and results <60):
    print(1)
elif(results >= 60 and results < 70):
    print(2)
elif(results >= 70 and results < 80):
    print(3)
elif(results >= 80 and results < 90):
    print(4)
elif(results >= 90 and results <= 100):
    print(5)
elif(results > 100):
    print("Impossible!")


print("")#Task18

fb = int(input("Enter number: "))
if(fb % 3 == 0 and fb % 5 == 0):
    print("FizzBuzz")
elif(fb % 3 == 0):
    print("Fizz")
elif(fb % 5 == 0):
    print("Buzz")


print("")#Task19

num = int(input("Please type in a number: "))
if(num > 0 and num % 2 == 0):
    print("The number is even")
elif(num <= 0):
    print("The number is negative or zero")
else:
    print("The number is odd")


print("")#Task20

year = int(input("Please type in a year: "))
leap = False
if(year % 400 == 0):
    print("That year is a leap year.")
elif(year % 100 == 0):
    print("That year is not a leap year.")
elif(year % 4 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")