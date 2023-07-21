def remove_duplicates_and_sort(words):
    # Split the input string into a list of words
    word_list = words.split()

    # Convert the list to a set to remove duplicates
    unique_words = set(word_list)

    # Sort the unique words alphabetically
    sorted_words = sorted(unique_words)

    return sorted_words

if __name__ == "__main__":
    input_sequence = input("Enter a sequence of whitespace-separated words: ")
    result = remove_duplicates_and_sort(input_sequence)
    print("Words after removing duplicates and sorting:")
    print(" ".join(result))
