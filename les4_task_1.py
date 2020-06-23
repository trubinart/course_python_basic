from sys import argv

def payroll(hours, money_in_hour, prize):
    print((hours + money_in_hour) + prize)

payroll(int(argv[1]), int(argv[2]), int(argv[3]))


