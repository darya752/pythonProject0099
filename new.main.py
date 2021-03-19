month = input('Enter the name of the month: ')
while True:
    try:
        income = int(input('Enter your estimated income: '))
        celebration = input('Are there any holidays this month? ')
    except ValueError:
        print('Enter an integer')
    else:
        break


def exp_yes(income):
    investment = round(float(income * 0.35), 1)
    utility_bills = round(float(income * 0.12), 1)
    transport = round(float(income * 0.05), 1)
    supermarkets = round(float(income * 0.1), 1)
    clothes = round(float(income * 0.1), 1)
    health_and_beauty = round(float(income * 0.1), 1)
    gifts = round(float(income * 0.1), 1)
    other_expenses = round(float(income * 0.08), 1)
    print('________________________________________________')
    print('|', month.upper(), '                     ')
    print('________________________________________________')
    print('| investment            |', investment)
    print('| utility bills         |', utility_bills)
    print('| transport             |', transport)
    print('| supermarkets          |', supermarkets)
    print('| clothes               |', clothes)
    print('| health and beauty     |', health_and_beauty)
    print('| gifts                 |', gifts)
    print('| other expenses        |', other_expenses)
    print('________________________________________________')


def exp_no(income):
    investment = round(float(income * 0.35), 1)
    utility_bills = round(float(income * 0.12), 1)
    transport = round(float(income * 0.05), 1)
    supermarkets = round(float(income * 0.1), 1)
    clothes = round(float(income * 0.1), 1)
    health_and_beauty = round(float(income * 0.1), 1)
    other_expenses = round(float(income * 0.08), 1)
    print('________________________________________________')
    print('|', month.upper(), '                     ')
    print('________________________________________________')
    print('| investment            |', investment)
    print('| utility bills         |', utility_bills)
    print('| transport             |', transport)
    print('| supermarkets          |', supermarkets)
    print('| clothes               |', clothes)
    print('| health and beauty     |', health_and_beauty)
    print('| other expenses        |', other_expenses)
    print('________________________________________________')


def exp_b_yes(income):
    investment = round(float(income * 0.4), 1)
    utility_bills = round(float(income * 0.07), 1)
    transport = round(float(income * 0.05), 1)
    supermarkets = round(float(income * 0.1), 1)
    clothes = round(float(income * 0.1), 1)
    health_and_beauty = round(float(income * 0.1), 1)
    gifts = round(float(income * 0.1), 1)
    other_expenses = round(float(income * 0.03), 1)
    print('________________________________________________')
    print('|', month.upper(), '                     ')
    print('________________________________________________')
    print('| investment            |', investment)
    print('| utility bills         |', utility_bills)
    print('| transport             |', transport)
    print('| supermarkets          |', supermarkets)
    print('| clothes               |', clothes)
    print('| health and beauty     |', health_and_beauty)
    print('| gifts                 |', gifts)
    print('| other expenses        |', other_expenses)
    print('________________________________________________')


def exp_b_no(income):
    investment = round(float(income * 0.4), 1)
    utility_bills = round(float(income * 0.07), 1)
    transport = round(float(income * 0.05), 1)
    supermarkets = round(float(income * 0.1), 1)
    clothes = round(float(income * 0.1), 1)
    health_and_beauty = round(float(income * 0.1), 1)
    other_expenses = round(float(income * 0.03), 1)
    print('________________________________________________')
    print('|', month.upper(), '                     ')
    print('________________________________________________')
    print('| investment            |', investment)
    print('| utility bills         |', utility_bills)
    print('| transport             |', transport)
    print('| supermarkets          |', supermarkets)
    print('| clothes               |', clothes)
    print('| health and beauty     |', health_and_beauty)
    print('| other expenses        |', other_expenses)
    print('________________________________________________')

if income == 3:
    print('Check the correctness of the entered data')
elif 80000 <= income < 85000 and celebration.lower() == 'yes':
    exp_yes(income)
elif 80000 <= income < 85000 and celebration.lower() == 'no':
    exp_no(income)
elif 85000 <= income < 200000 and celebration.lower() == 'yes':
    exp_b_yes(income)
elif 85000 <= income < 200000 and celebration.lower() == 'no':
    exp_b_no(income)

