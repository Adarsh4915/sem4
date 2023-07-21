def find_smallest_recursive(input_list):
    if len(input_list) == 1:
        return input_list[0]
    else:
        smaller_element = find_smallest_recursive(input_list[1:])
        return input_list[0] if input_list[0] < smaller_element else smaller_element

if __name__ == "__main__":
    input_list = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
    smallest = find_smallest_recursive(input_list)
    print("Smallest element in the list:", smallest)
