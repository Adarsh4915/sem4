def find_length_recursive(input_string):
    if not input_string:
        return 0
    else:
        return 1 + find_length_recursive(input_string[1:])

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    length = find_length_recursive(input_string)
    print("Length of the string:", length)
