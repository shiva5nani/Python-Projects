def replace_word_in_file(filename, old_word, new_word):
    try:
        
        with open(filename, "r") as file:
            content = file.read()

        if old_word not in content:
            print(f"The word '{old_word}' was not found in the file.")
            return

       
        updated_content = content.replace(old_word, new_word)

        
        with open(filename, "w") as file:
            file.write(updated_content)

        print("File updated successfully.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def main():
    print("=== Find and Replace Program ===")

    file_name = input("Enter the file name (e.g., sample.txt): ")
    word_to_find = input("Enter the word to find: ")
    replacement_word = input("Enter the replacement word: ")

    replace_word_in_file(file_name, word_to_find, replacement_word)


main()
