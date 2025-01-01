from controller import run


def run_test_cases_1():
    #################################################################################################################
    # Invalid card number
    # 1. only 15 digit while needs 16 digits
    # 2. includes other character
    test_inputs = [{"card_info": ["784556471984750", "smith", "12312026"]}]
    run(test_inputs=test_inputs)
    test_inputs = [{"card_info": ["784556471984750-", "smith", "12312026"]}]
    run(test_inputs=test_inputs)

    ################################################################################################################
    # Invalid valid_date
    # 1. only 5 digits while needs 8 digits
    # 2. includes other characters
    # 3. expired
    test_inputs = [{"card_info": ["7845564719847501", "smith", "1231202"]}]
    run(test_inputs=test_inputs)
    test_inputs = [{"card_info": ["7845564719847501", "smith", "1231202-"]}]
    run(test_inputs=test_inputs)
    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312024"]}]
    run(test_inputs=test_inputs)

    #################################################################################################################
    # # Card is not exist
    # # 1. wrong account number
    # # 2. wrong owner name
    test_inputs = [{"card_info": ["7845564719847502", "smith", "12312026"]}]
    run(test_inputs=test_inputs)
    test_inputs = [{"card_info": ["7845564719847501", "john", "12312026"]}]
    run(test_inputs=test_inputs)


def run_test_cases_2():
    ################################################################################################################
    # Invalid PIN
    # 1. only 5 digits while needs 6 digits, includes other characters until 5 times
    # 2. wrong PIN until 5 times, inactivate card
    # 3. check the inactivation
    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["43212", "43212", "43212", "43212-", "43212-"]}]
    run(test_inputs=test_inputs)

    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["43212", "43212", "43212", "43212-", "432125", "432125", "432125", "432125", "432125"]}]
    run(test_inputs=test_inputs)
    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"], "pin": ["432126"]}]
    run(test_inputs=test_inputs)


def run_test_cases_3():
    ##################################################################################################################
    # Invalid account_number_answer
    # 1. Invalid account_number_answer
    # 2. No account_number_answer
    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["432126"],
                    "account_number_answer": "1"}]
    run(test_inputs=test_inputs)
    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["432126"],
                    "account_number_answer": "n"}]
    run(test_inputs=test_inputs)

    ##################################################################################################################
    # Invalid task answer
    # 1. Invalid task answer
    # 2. Invalid more task answer
    # 3. Multiple task & No more task
    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["432126"],
                    "account_number_answer": "y",
                    "task_answer_list": ["0"]}]
    run(test_inputs=test_inputs)

    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["432126"],
                    "account_number_answer": "y",
                    "task_answer_list": ["1"],
                    "more_task_answer_list": ["a"]}]
    run(test_inputs=test_inputs)

    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["432126"],
                    "account_number_answer": "y",
                    "task_answer_list": ["1", "1"],
                    "more_task_answer_list": ["y", "n"]}]
    run(test_inputs=test_inputs)

    #################################################################################################################
    # Check deposit
    # 1. Invalid answer
    # 2. Multiple No
    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["432126"],
                    "account_number_answer": "y",
                    "task_answer_list": ["2"],
                    "deposit_answer_list": [["y1"]],
                    "more_task_answer_list": ["n"]}]
    run(test_inputs=test_inputs)

    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["432126"],
                    "account_number_answer": "y",
                    "task_answer_list": ["2"],
                    "deposit_answer_list": [["n", "n", "n", "n", "n"]],
                    "more_task_answer_list": ["n"]}]

    run(test_inputs=test_inputs)

    ##################################################################################################################
    # Check deposit, withdraw
    # Check withdraw
    # 1. Invalid answer
    # 2. Exceed balance, Exceed multiple trials
    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["432126"],
                    "account_number_answer": "y",
                    "task_answer_list": ["3"],
                    "withdraw_answer_list": [["y1"]],
                    "more_task_answer_list": ["n"]}]
    run(test_inputs=test_inputs)

    test_inputs = [{"card_info": ["7845564719847501", "smith", "12312026"],
                    "pin": ["432126"],
                    "account_number_answer": "y",
                    "task_answer_list": ["3", "3"],
                    "withdraw_answer_list": [["700", "100"], ["700", "700"]],
                    "more_task_answer_list": ["y", "y", "y"]}]
    run(test_inputs=test_inputs)


if __name__ == "__main__":
    # Try one by one
    run_test_cases_1()
    # run_test_cases_2()
    # run_test_cases_3()

    # For interactive running with console
    # run()
