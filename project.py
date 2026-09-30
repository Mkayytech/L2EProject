def budget_remaining(budget, food, transport):
    return budget - (food + transport)

def budget_message(name, remaining):
    return f"{name} has {remaining} naira remaining."

print("---Normal Test Case---")
section_1 = budget_remaining(5000, 1500, 2000)
section_1_message = budget_message("Muffin", section_1)
print(section_1)
print(section_1_message)