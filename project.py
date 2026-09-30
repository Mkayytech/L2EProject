def budget_remaining(budget, food, transport):
    return budget - (food + transport)

def budget_message(name, remaining):
    return f"{name}, you have {remaining} naira remaining."