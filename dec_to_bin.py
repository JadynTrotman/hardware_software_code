def decmial_to_binary(number):
    number = int(number)
    result = ""
    while number > 0:               #keep dividing until at 0
        remainder = number % 2
        number = number // 2
        result = str(remainder) + result #place string in reverse order
    return result


def main():
    num = input("Enter Decimal Number:")
    print("Decmial {} to Binary: {}".format(num, decmial_to_binary(num)))

if __name__ == "__main__":
    main()
