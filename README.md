# Simple ATM Controller

Implementation of a simple atm controller

## Environment
Developed in python3.8, Windows 10 Pro

## How To Run
In test.py try each...
- run_test_cases_1()
- run_test_cases_2()
- run_test_cases_3()
- run()

## Work Flow
1. Check the validity of the card number
2. Check the validity of the validation date
3. Check the card is registered with card number and owner name
4. Check the validity of the PIN
5. Check whether the PIN is correct (If wrong too much, card can be inactivated)
6. Ask whether the account number is correct
7. Ask what you want to do
8. Action
9. Ask if you want more action

## Details
- controller.py works as main function for an atm controller
- Predefined cards are save in "check_valid.py"
- Predefined accounts are save in "account.py"

## Example Result
![image](https://github.com/user-attachments/assets/11bf0a8e-21ff-4af3-8ee9-cb3e018e67bd)
