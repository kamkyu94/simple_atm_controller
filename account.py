# Registered Accounts
import time


# May not be used in the future
valid_accounts = {"2934208175897": {"balance": 500,
                                    "pw": 1228,
                                    "pin_mistake_cnt": 0,
                                    "activated": True},

                  "1705184175324": {"balance": 1000,
                                    "pw": 2897,
                                    "pin_mistake_cnt": 0,
                                    "activated": True},
                  }


# May not be used in the future
def print_wrong_answer(answer):
    print("================================================")
    print("Wrong answer input: \"%s\". In ATM there would be only valid buttons in the display." % answer)
    print("This kind of case would not happen. We added this just in case for the test.")
    print("================================================\n")


def print_finished():
    print("================================================")
    print("Prepared \"test_input\" is finished. This will not happen win real situation.")
    print("Because we will wait until the customer enter the key. (Ex. by using input() function.")
    print("================================================\n")


# Now we fix the every deposit amount as $100
# Need to change in the future.
def count_cash():
    return 100


# Now the accounts are declared as dictionary in this code, and we check the balance with the dictionary.
# Need to change in the future.
def balance(account_number):
    print("================================================")
    print("In your account: %s" % account_number)
    print("You have $%d." % valid_accounts[account_number]["balance"])
    print("================================================\n")


# Now the accounts are declared as dictionary in this code, and we deposit the cash with the dictionary.
# Need to change in the future.
def deposit(account_number, max_trial, test_input):
    counter = 0
    while True:
        # Receive and count the cash
        print("\nPlease put the cash.")
        print("Now counting...\n")
        time.sleep(1)
        cash = count_cash()

        # Check the amount of cash
        print("Is this the amount you want to deposit? $%d (y/n)" % cash)
        if test_input is None:
            answer = input("Enter the answer (y/n) :>> ")
        else:
            answer = test_input[counter]
            print("Got: %s" % answer)

        if answer == "y":
            valid_accounts[account_number]["balance"] += cash
            print("================================================")
            print("Now in your account: %s" % account_number)
            print("You have $%d." % valid_accounts[account_number]["balance"])
            print("================================================\n")
            return 1
        elif answer == "n":
            print("Okay. Please try again")
        else:
            print_wrong_answer(answer)
            return -1

        counter += 1
        if counter == max_trial:
            print("\n================================================")
            print("Exceed max trial.")
            print("Please try again from the beginning.")
            print("================================================")
            return -1

        # Check finish of the prepared "test_input"
        if test_input is not None and counter == len(test_input) - 1:
            print_finished()
            return -1


def withdraw(account_number, max_trial, test_input):
    counter = 0
    while True:
        # Check the amount of cash
        print("\nHow much do you want to withdraw?")

        if test_input is None:
            answer = input("Enter the answer :>> ")
        else:
            answer = test_input[counter]
            print("Got: %s" % answer)

        # Check the answer
        if not answer.isdecimal():
            print_wrong_answer(answer)
            return -1

        answer = int(answer)

        # Check with the balance
        if valid_accounts[account_number]["balance"] < answer:
            print("================================================")
            print("Not enough balance to withdraw: $%d" % answer)
            print("In your account: %s" % account_number)
            print("You have $%d." % valid_accounts[account_number]["balance"])
            print("Please try again.")
            print("================================================\n")
            counter += 1
        else:
            print("================================================")
            valid_accounts[account_number]["balance"] -= answer
            print("Withdraw: $%d" % answer)
            print("Now in your account: %s" % account_number)
            print("You have $%d." % valid_accounts[account_number]["balance"])
            print("================================================\n")
            return 1

        if counter == max_trial:
            print("================================================")
            print("Exceed max trial.")
            print("Please try again from the beginning.")
            print("================================================")
            return -1

        # Check finish of the prepared "test_input"
        if test_input is not None and counter == len(test_input):
            print_finished()
            return -1
