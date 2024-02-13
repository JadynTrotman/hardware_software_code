def decimal_to_binary(number):
    number = (int(number))
    result = ""
    while number > 0:               #keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result #place string in reverse order
    return result


def main():
    while True:
        try:
            num = int(input("Enter Decimal Number:"))
        except ValueError:
            print("Invalid, not a decimal number")
        else:
            print("Decimal {} to Binary: {}".format(num, decimal_to_binary(num)))
            continue


if __name__ == "__main__":
    main()
