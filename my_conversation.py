def conversation():
    print("Do you like coding in python? Answer yes or no")
    answer = input()
    if answer == "yes":
       print("That's good - the united states needs more coders!!")
    else:
       if answer == "no":
        print("Perhaps you will change your mind")
       else:
        print("I do not understand your answer")
    print("Goodbye")

def main():
    print("Welcome to my conversation program")
    conversation()
    print("Thanks for chatting with me")

if __name__ == "__main__":
    main()
