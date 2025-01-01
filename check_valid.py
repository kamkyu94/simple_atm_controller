import random
from datetime import datetime


# Registered Cards
# May not be used in the future
valid_cards = {"7845564719847501": {"owner_name": "smith",
                                    "account_number": "2934208175897",
                                    "pin": "432126",
                                    "pin_mistake_cnt": 0,
                                    "activated": True},

               "8170921309843896": {"owner_name": "john",
                                    "account_number": "1705184175324",
                                    "pin": "1254631",
                                    "pin_mistake_cnt": 0,
                                    "activated": True},

               "5421265267072315": {"owner_name": "sarah",
                                    "account_number": None,
                                    "pin": "9086233",
                                    "pin_mistake_cnt": 0,
                                    "activated": False}
               }


# Check the validity of the inserted card_info
def card_is_valid(card_number, valid_until, office_number):
    # Check card number
    if len(card_number) != 16 or not card_number.isdecimal():
        print("================================================")
        print("We have got invalid card number.")
        print("We think the card is damaged or the card reader in our ATM is malfunctioned.")
        print("Please try again.")
        print("If you think this is the problem of the machine, please call to %s." % office_number)
        print("================================================\n")
        return False

    # Check validation date 1
    if len(valid_until) != 8 or not valid_until.isdecimal():
        print("================================================")
        print("We have get invalid validation date of the card.")
        print("We think the card is damaged or the card reader in our ATM is malfunction.")
        print("Please try again.")
        print("If you think this is the problem of the machine, please call to %s." % office_number)
        print("================================================\n")
        return False

    # Check validation date 2
    now = datetime.now()
    now_day, now_month, now_year = now.day, now.month, now.year
    valid_day, valid_month, valid_year = valid_until[0:2], valid_until[2:4], valid_until[4:]

    passed = False
    if int(now_year) > int(valid_year):
        passed = True
    if not passed and int(now_month) > int(valid_month):
        passed = True
    if not passed and int(now_day) > int(valid_day):
        passed = True
    if passed:
        print("================================================")
        print("Your card is expired.")
        print("Please reissue the card.")
        print("Current date: %s/%s/%s (day/month/year)" % (now_day, now_month, now_year))
        print("Card is valid until: %s/%s/%s (day/month/year)" % (valid_day, valid_month, valid_year))
        print("================================================\n")
        return False

    return True


# Check the validity of the server.
# Now we randomly decide the validity of the server. There is 1 % of probability in malfunctioning.
# Need to change in the future.
def server_is_valid(address):
    if random.random() < 0.99:
        message_from_server = "Okay"
    else:
        message_from_server = "Updating" if random.random() < 0.5 else "Malfunctioning"

    if message_from_server != "Okay":
        print("================================================")
        print("Now the bank system is %s." % message_from_server)
        print("Please try later.")
        print("================================================\n")
        return False

    return True


# Check whether the card is register in the bank.
# Now the cards are declared as dictionary in this code, and we check the card with the dictionary.
# Need to change in the future.
def card_is_exist(card_number, owner_name, server_address):
    if card_number not in valid_cards or owner_name != valid_cards[card_number]["owner_name"]:
        print("================================================")
        print("This card is not registered in our bank.")
        print("Please check the card again and insert the right one.")
        print("================================================\n")
        return False

    if valid_cards[card_number]["account_number"] is None:
        print("================================================")
        print("This card has no connected account.")
        print("Please visit to the bank or use our online PC/mobile bank to connect the account.")
        print("================================================\n")
        return False

    if not valid_cards[card_number]["activated"]:
        print("================================================")
        print("This card is inactivated.")
        print("Please visit to the bank to reactivate.")
        print("================================================\n")
        return False

    return True


# Check the validity of the inserted PIN
def pin_is_valid(pin):
    if len(pin) != 6 or not pin.isdecimal():
        return False
    return True


# Check the PIN
# Now the cards are declared as dictionary in this code, and we check the PIN with the dictionary.
# Need to change in the future.
def check_pin(card_number, pin, max_mistakes, server_address):
    if pin != valid_cards[card_number]["pin"]:
        valid_cards[card_number]["pin_mistake_cnt"] += 1
        left_chance = max_mistakes - valid_cards[card_number]["pin_mistake_cnt"]

        if left_chance > 0:
            print("PIN is wrong. After %d more mistakes, your card will be inactivated." % left_chance)
            print("Please try again.")
            return 0
        else:
            valid_cards[card_number]["activated"] = False
            print("================================================")
            print("This card is now inactivated.")
            print("Please visit to the bank to reactivate.")
            print("================================================\n")
            return -1

    valid_cards[card_number]["pin_mistake_cnt"] = 0
    return valid_cards[card_number]["account_number"]
