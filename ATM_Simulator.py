import sys

user_line = 0
status = ""
accountRecords = open("ATM_accounts.csv", "r+")

class accountHolder:
    def __init__(self, userID):
        self.title = ""
        self.fname = ""
        self.sname = ""
        self.ID = userID
        self.balance = ""
        self.value = ""
        self.option = ""

def menu(user_line):
    print(f"\nLogged in as: {user.title} {user.fname[0]} {user.sname}\n")
    menuOption = ""
    while menuOption != "1" and menuOption != "2" and menuOption != "3" and menuOption != "4" and menuOption != "5":
        print("    **MENU**\n1 - Display Balance\n2 - Withdraw funds\n3 - Deposit funds\n4 - Return card\n5 - Exit\n\n")
        menuOption = input("Select an option (1-5): ")
        if menuOption != "1" and menuOption != "2" and menuOption != "3" and menuOption != "4" and menuOption != "5":
            print("ERROR! Invalid option.\n")

    if menuOption == "1":
        displayBalance()
    elif menuOption == "2":
        withdraw(user_line)
    elif menuOption == "3":
        deposit(user_line)
    elif menuOption == "4":
        returnCard()
    elif menuOption == "5":
        print("Thank you for using our service.\nExiting application...\n.\n.\n.\n.\n.")
        sys.exit()

def update(user_line):
    accountRecords.seek(0)
    line = -1
    item = 0
    for lines in accountRecords:
        line += 1
        if line == user_line:
            for items in lines.split():
                item += 1
                if item == 2:
                    user.title = items
                elif item == 3:
                    user.fname = items
                elif item == 4:
                    user.sname = items
                elif item == 5:
                    user.balance = items
                    break

def getAmount():
    amount = {
        "0": "Back",
        "1": "5",
        "2": "10",
        "3": "15",
        "4": "20",
        "5": "25",
        "6": "30",
        "7": "50",
        "8": "100",
        "9": "200",
        "10": "Other"
    }
    user.value = amount.get(user.option, "")
    return user.value

def displayBalance():
    print("Your available balance is: £%s" % (user.balance))

def withdraw(user_line):
    accountRecords.seek(0)
    data = accountRecords.read()
    user.option = ""
    check = "."
    alphabet = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("\nSelect the amount you wish to withdraw...\n\n0 - Back to Menu     5 - £25         10 - Other\n\n1 - £5               6 - £30\n\n2 - £10              7 - £50\n\n3 - £15              8 - £100\n\n4 - £20              9 - £200")
    while user.option != "1" and user.option != "2" and user.option != "3" and user.option != "4" and user.option != "5" and user.option != "6" and user.option != "7" and user.option != "8" and user.option != "9" and user.option != "10":
        user.option = input("\nInsert option here [0-10]: ")
        if user.option != "0" and user.option != "1" and user.option != "2" and user.option != "3" and user.option != "4" and user.option != "5" and user.option != "6" and user.option != "7" and user.option != "8" and user.option != "9" and user.option != "10":
            print("Invalid option. Please try again...")
        else:
            getAmount()
            if user.value == "Back":
                print("Returning to main menu...\n")
                break
            elif user.value == "Other":
                while check == "." or check == "false":
                    if check == "false":
                        print("ERROR! Invalid amount.\n")
                        check = "."
                    user.value = input("Enter the amount to withdraw: £")
                    for i in user.value:
                        for j in alphabet:
                            if i == j.lower() or i == j.upper():
                                check = "false"
                            elif i == user.value[len(user.value) - 1] and j == "Z" and check != "false":
                                check = "true"

            if float(user.value) > float(user.balance):
                print("Insufficient funds!")
                user.value = ""
            else:
                f = float(user.balance) - float(user.value)
                newBalance = "%.2f" % (f)
                newData = data.replace(user.balance, newBalance)
                s = open("ATM_accounts.csv", "w")
                s.write(newData)
                s.close()
                update(user_line)
                print(f"\nYou have withdrawn:       £{user.value}\nYour new balance is:      £{user.balance}")
                break

def deposit(user_line):
    accountRecords.seek(0)
    data = accountRecords.read()
    check = "."
    alphabet = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while check == "." or check == "false":
        if check == "false":
            print("ERROR! Invalid amount.\n")
            check = "."
        user.value = input("Enter the amount to deposit: £")
        for i in user.value:
            for j in alphabet:
                if i == j.lower() or i == j.upper():
                    check = "false"
                elif i == user.value[len(user.value) - 1] and j == "Z" and check != "false":
                    check = "true"
    else:
        if float(user.value) > float(user.balance):
            print("Insufficient funds!")
            user.value = ""
        else:
            f = float(user.balance) + float(user.value)
            newBalance = "%.2f" % (f)
            newData = data.replace(user.balance, newBalance)
            s = open("ATM_accounts.csv", "w")
            s.write(newData)
            s.close()
            update(user_line)
            print(f"\nYou have deposited:       £{user.value}\nYour new balance is:      £{user.balance}")

def returnCard():
    print("\nThank you for using our service!\nLogging out...\nPlease take your card\n.\n.\n.\n.\n.\n.\n.")
    reset()

def reset():
    user.title = ""
    user.fname = ""
    user.sname = ""
    user.ID = ""
    user.balance = ""
    user.value = ""
    user.option = ""

def main(user_line):
    global user, status, accountRecords
    while status == "":
        accountRecords.seek(0)
        index = len(accountRecords.readlines())
        accountRecords.seek(0)
        user_line = 0
        userID = input("\nWelcome to Kenny's ATM\n\nPlease enter your ID number:  ")
        for line in accountRecords:
            user_line += 1
            if userID in accountRecords.read(4) and len(userID) == 4:
                print(user_line)
                user = accountHolder(userID)
                update(user_line)
                status = "Active"
                break
            elif user_line == index - 1:
                print("INVALID ID.\n")

    while status == "Active":
        menu(user_line)
        if userID != user.ID:
            status = ""
            main(user_line)
            break
        else:
            newOption = ""
            while newOption.lower() != "n" and newOption.lower() != "no" and newOption.lower() != "y" and newOption.lower() != "yes":
                newOption = input("\nWould you like another service? Y/N : ")
                if newOption.lower() == "n" or newOption.lower() == "no":
                    returnCard()
                    status = ""
                    main(user_line)


if __name__ == "__main__":
    main(user_line)
