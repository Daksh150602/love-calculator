def calculate_love_score(name_1, name_2):
    defination = "truelove"
    combine_name = name_1 + name_2
    total = 0
    for char in combine_name:
        if char in defination:
            total+= 1
    return total


name_1 = input()
name_2 = input()
score=calculate_love_score(name_1, name_2)
print(f"your compatibility is {score} no.")
