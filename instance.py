from user_input_validator import UserInputValidator

def main():
    validator1 = UserInputValidator()
    Validator2 = UserInputValidator()

    list_one = ["4", "-7", "a", "0", "100"]
    list_two = ["67", "b", "-2", "1", "8"]

    result_one = validator1.validate_positive_integers(list_one)
    print("Valid numbers from first list:", result_one)
    print()

    result_two = Validator2.validate_positive_integers(list_two)
    print("Valid numbers from second list:", result_two)

if __name__ == "__main__":
    main()