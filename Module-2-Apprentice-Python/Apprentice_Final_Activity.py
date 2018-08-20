import operator

saved_string = ''


def remove_letter(): #Remove a selected letter from a string
    print "\nRemove Letter"

    global saved_string

    while True:
        prompt_input = raw_input("Enter a letter to remove from word - %s: " % saved_string)
        if len(prompt_input) == 1:
            break
        print "Error! Only one letter allowed!"

    saved_string = str(saved_string).replace(prompt_input, "")
    print "The saved string is now: %s" % saved_string


def num_compare(): #Compare 2 numbers to determine the larger
    print "\nNum Compare"

    input_one = int(raw_input("Enter first number: "))
    input_two = int(raw_input("Enter second number: "))

    print "The largest of numbers of %d and %d is: %d" % (input_one, input_two, max(input_one, input_two))


def print_string(): #Print the previously stored string
    print "\nPrint String"

    print saved_string


def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
    print "\nCalculator"

    return


def accept_and_store(): #Accept and store a string
    print "\nAccept and Store"
    global saved_string
    saved_string = str(raw_input("Enter string to save: "))

    print "You saved the following word: %s" % str(saved_string)


def main(): #menu goes here
    # Stores function addresses, which can be invoked later.
    options_list = [remove_letter,
                    num_compare,
                    print_string,
                    calculator,
                    accept_and_store]
    while True:
        print "\nSELECT OPTIONS:"
        print "1\tRemove Letter"
        print "2\tNum Compare"
        print "3\tPrint String"
        print "4\tCalculator"
        print "5\tAccept and Store"
        print "\n0\tExit"

        options_choice = int(raw_input("SELECTION: ")) - 1
        if options_choice == -1:
            break
        else:
            options_list[options_choice]()


main()
