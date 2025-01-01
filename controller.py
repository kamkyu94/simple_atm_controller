from account import *
from settings import *
from check_valid import *


# We may update the several settings by asking the bank server when the ATM turns on.
# Need to change in the future.
def update():
    office_number = "891-387-2965"
    max_mistakes = 5
    max_trial = 5
    time.sleep(1)
    return office_number, max_mistakes, max_trial


def main_controller(office_number, max_mistakes, max_trial, test_input=None):
    ##################################################################################################################
    # Step 1: Insert Card ============================================================================================
    print("\n\n\n################################################")
    print("Running ATM")
    print("################################################\n")
    print("Please Insert Your Card...")
    if test_input is None:
        card_info = input("Recommend: 7845564719847501 smith 12312026\nEnter the card info :>> ")
        card_number, owner_name, valid_until = card_info.split(" ")
    else:
        card_number, owner_name, valid_until = test_input["card_info"]
        print("Got: %s %s %s" % (card_number, owner_name, valid_until))

    # Check validity of the card_info
    if not card_is_valid(card_number, valid_until, office_number):
        return -1

    # Check validity of the server
    if not server_is_valid(address=server_address):
        return -1

    # Check the connected bank and bank account
    if not card_is_exist(card_number, owner_name, server_address):
        return -1

    ##################################################################################################################
    # Step 2: Insert PIN =============================================================================================
    print("\nPlease Enter your PIN...")
    pin, counter_1 = None, 0
    while True:
        if counter_1 >= max_mistakes:
            print("================================================")
            print("You have made too many mistake.")
            print("Please try again from the beginning.")
            print("================================================\n")
            return -1

        if test_input is None:
            pin = input("Recommend: 432126\nEnter the PIN :>> ")
        else:
            pin = test_input["pin"][counter_1]
            print("Got: %s" % pin)

        if not pin_is_valid(pin):
            counter_1 += 1
            print("PIN should be in 6 digits. Please enter again. (%d / %d)" % (counter_1, max_mistakes))
        else:
            break

    counter_2 = 0
    while True:
        account_number = check_pin(card_number, pin, max_mistakes, server_address)

        if account_number == 0:
            counter_2 += 1
        elif account_number == -1:
            return -1
        else:
            break

        if test_input is None:
            pin = input("Recommend: 432126\nEnter the PIN :>> ")
        else:
            pin = test_input["pin"][counter_1 + counter_2]
            print("Got: %s" % pin)

    ##################################################################################################################
    # Step 3: Select account =========================================================================================
    print("\nIs this account number \"%s\" correct? Yes: \"y\", No: \"n\"" % account_number)
    if test_input is None:
        answer = input("Enter the answer (y/n) :>> ")
    else:
        answer = test_input["account_number_answer"]
        print("Got: %s" % answer)

    if answer == "n":
        print("================================================")
        print("You refused to use the account number \"%s\"" % account_number)
        print("See you next time.")
        print("================================================\n")
        return -1
    elif answer != "y":
        print_wrong_answer(answer)
        return -1

    ##################################################################################################################
    # Step 4: Balance/Deposit/Withdraw ===============================================================================
    counter = 0
    while True:
        # Step 4-1 ===================================================================================================
        print("\nWhich task do you want to do? Balance: \"1\", Deposit: \"2\", Withdraw: \"3\"")

        if test_input is None:
            answer = input("Enter the answer (1/2/3) :>> ")
        else:
            answer = test_input["task_answer_list"][counter]
            print("Got: %s" % answer)

        # Balance
        if answer == "1":
            balance(account_number)
        # Deposit
        elif answer == "2":
            t_i = None if test_input is None else test_input["deposit_answer_list"][counter]
            if deposit(account_number, max_trial, t_i) == -1:
                return -1
        # Withdraw
        elif answer == '3':
            t_i = None if test_input is None else test_input["withdraw_answer_list"][counter]
            if withdraw(account_number, max_trial, t_i) == -1:
                return -1
        else:
            print_wrong_answer(answer)
            return -1

        # Step 4-2 ===================================================================================================
        print("Do you want to do something more? Yes: \"y\", No: \"n\"")

        if test_input is None:
            answer = input("Enter the answer (y/n) :>> ")
        else:
            answer = test_input["more_task_answer_list"][counter]
            print("Got: %s" % answer)

        if answer == "n":
            print("\n================================================")
            print("Thank you for using. Please take your card safe.")
            print("See you next time.")
            print("================================================\n")
            return -1
        elif answer != "y":
            print_wrong_answer(answer)
            return -1

        # Check finish of the prepared "test_input"
        counter += 1
        if test_input is not None and counter == len(test_input["task_answer_list"]):
            print_finished()
            return -1


def run(test_inputs=None):
    # Turn on the ATM
    office_number, max_mistakes, max_trial = update()

    # Run
    if test_inputs is not None:
        for t_i in test_inputs:
            main_controller(office_number, max_mistakes, max_trial, t_i)
    else:
        while True:
            main_controller(office_number, max_mistakes, max_trial, None)
