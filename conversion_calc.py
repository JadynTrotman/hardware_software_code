def intro_msg(): #opening statement of code
    print("Hello")
    print("This program converts decimal numbers to binary and binary numbers to decimal")
    print("Option 1 is Binary to decimal and option 2 is Decimal to binary")
    print("The program will then perform a calculation of either option then return to option select")
    print("To exit program enter the number 3 in option select")
    return input("To start a calculation select option 1 or 2")

def display_calc(): # used to display a menu
    calc_dict = {
        '1':'Binary to decimal',
        '2':'Decimal to binary',
        '3':'Exit/Cancel',
    }
    return calc_dict


def calc_options(): #codes options
    calc_dict = int(input("Enter your option: "))
    while calc_dict != 0:
        if calc_dict == 1:
            #do option 1 stuff
            print("Binary to decimal has been called.")
            pass
            check_int_bin()
        elif calc_dict == 2:
            #do option 2 stuff
            print("Decimal to binary has been called.")
            check_int_dec()
            pass
        elif calc_dict == 3:
            #do option 3 stuff
            print("Exiting program")
            break
        else:
            print("Invalid option.")
        break

def binary_to_decimal(number):
    decimal = 0
    power = 1
    while number>0: # Find the remainder of the given binary number.
        rem = number%10
        number = number//10
        decimal += rem*power # For every remainder multiply it with the power of 2.
        power = power*2
    return decimal

def check_int_bin():
    while True:
        try:
             num = int(input("Enter Binary Number:"))
        except ValueError:
            print("Invalid, not a Binary number")
        else:
            print("Binary {} to Decimal: {}".format(num, binary_to_decimal(num)))
            return calc_options()

def decimal_to_binary(number):
    number = (int(number))
    result = ""
    while number > 0:               #keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result #place string in reverse order
    return result

def check_int_dec():
    while True:
        try:
             num = int(input("Enter Decimal Number:"))
        except ValueError:
            print("Invalid, not a Decimal number")
        else:
            print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))
            return calc_options()


def main():
    word = intro_msg()
    word = display_calc()
    word = calc_options()
    print('Thank you for using this program \n'.format())

if __name__ == '__main__':
    main()
