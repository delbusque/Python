def my_choice():

    right_digit = False
    right_range = range(1, 10)
    choice = 0

    while right_digit == False:

        input_choice = input('Enter a number in range (1-10): ')

        if input_choice.isdigit():
            if (int(input_choice) in right_range):
                right_digit = True
                print('YES !')
                choice = int(input_choice)
            else:
                print('Not correct RANGE !')
        else:
            print('Not correct input !')

    return choice


my_choice()
