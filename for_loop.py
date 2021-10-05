#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program uses a for loop
#   with user input


def main():
    # this function uses a for loop
    loop_counter = 0
    total = 0

    # input
    user_number_as_string = input("Enter an integer >= 0: ")
    print("")

    # process & output
    try:
        user_number_as_integer = int(user_number_as_string)
        if user_number_as_integer < 0:
            print("{0} is a negative integer.".format(user_number_as_string))

        else:
            for loop_counter in range(user_number_as_integer + 1):
                total = loop_counter ** 2
                print("{0}² = {1}".format(loop_counter, total))

    except Exception:
        print("{0} is not an integer.".format(user_number_as_string))

    print("\nDone.")


if __name__ == "__main__":
    main()
