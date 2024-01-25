def check_selection(numbers): #verify if it is a hexidecimal
    hex_list =["A", "B", "C", "D", "E", "F", "0", "1",
               "2", "3", "4", "5", "6", "7", "8", "9"]
    for number in numbers:
        if number.upper() not in hex_list: #check if number is  not in hex list
            print("Not a hexidecimal number")
            return(False)
    return(True)

def main():
    good_selection = False
    while not good_selection:
        selection = input("Provide a hexidecimal number:")
        good_selection = check_selection(selection)
    print("Good job", selection, "is a hexidecimal number!!!")


    if __name__ == "__main__":
        main()
