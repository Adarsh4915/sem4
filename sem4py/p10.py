def copy_odd_lines(source_file, target_file):
    try:
        with open(source_file, 'r') as source:
            with open(target_file, 'w') as target:
                lines = source.readlines()
                odd_lines = [line for i, line in enumerate(lines) if i % 2 == 0]
                target.writelines(odd_lines)
        print("Odd lines copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    source_file_name = input("Enter the source file name: ")
    target_file_name = input("Enter the target file name: ")

    copy_odd_lines(source_file_name, target_file_name)
