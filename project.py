# Budget	Food	Transport	Expected result
# 5000 1500 2000 1500
# 5000 0    0    5000
# 5000 3500 4500 -3000

def budget_remaining(budget, food, transport):
    return budget - (food + transport)

def budget_message(name, remaining):
    return f"{name} has {remaining} naira remaining."

print("---Normal Test Case---")
section_1 = budget_remaining(5000, 1500, 2000)
section_1_message = budget_message("Muffin", section_1)
print(section_1)
print(section_1_message)

print("---Overspent Test Case---")
section_2 = budget_remaining(5000, 3500, 4500)
section_2_message = budget_message("Muffin", section_2)
print(section_2)
print(section_2_message)