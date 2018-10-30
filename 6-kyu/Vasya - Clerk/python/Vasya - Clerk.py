# My Solution
TICKET_MONEY = 25


def tickets(people):
    people = sorted(people)
    have_money = {25: 0, 50: 0, 100: 0}
    for money in people:
        if check_money(money, have_money):
            have_money[money] += 1
        else:
            return "NO"
    return "YES"


def check_money(money, have_money):
    if money == TICKET_MONEY:
        return True
    elif money == 50 and have_money[TICKET_MONEY] > 0:
        have_money[TICKET_MONEY] -= 1
        return True
    elif money == 100 and have_money[TICKET_MONEY] > 0:
        if have_money[50] > 0:
            have_money[TICKET_MONEY] -= 1
            have_money[50] -= 1
        elif have_money[TICKET_MONEY] > 3:
            have_money[TICKET_MONEY] -= 3
        else:
            return False
        return True
    return False


# Best Practice & Clever
def tickets(people):
    till = {100.0:0, 50.0:0, 25.0:0}

    for paid in people:
        till[paid] += 1
        change = paid-25.0
    
    for bill in (50,25):
        while (bill <= change and till[bill] > 0):
            till[bill] -= 1
            change -= bill

    if change != 0:
        return 'NO'
        
    return 'YES'