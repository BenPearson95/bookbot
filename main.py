def main():
    with open("books/frankenstein.txt") as f:
        
        # Read the contents of the file
        file_contents = f.read()

        # Get the words by splitting each character into an array and then using len()
        word_length = len(file_contents.split())

        # Create a dictionary with the structure {char: num} i.e {'a': 5}
        char_count_dict = charCounter(file_contents)

        # Expand the dictionary so each entry is converted into it's own dictionary
        # This has the structure {char: char, num: num}, i.e {char: a, num: 5}
        # Append this result to an array
        expanded_char_count_array = expand_dictionary(char_count_dict)

        # Sort the array, highest first.
        expanded_char_count_array.sort(reverse=True, key=sort_on)

        # Print the report in it's entirity. 
        print_report(word_length, expanded_char_count_array)

        

        


def charCounter(string):
    string = string.lower()
    charDict = {}
    for char in string:
        if (char in charDict):
            charDict[char]+= 1
        else:
            charDict[char] = 1
    return charDict

def expand_dictionary(dictionary):
    expanded_dictionary_array = []
    for char in dictionary:
            expanded_dictionary = {}
            if(char.isalpha()):
                expanded_dictionary['char'] = char
                expanded_dictionary['num'] = dictionary[char]
                expanded_dictionary_array.append(expanded_dictionary)

    return expanded_dictionary_array

def sort_on(dict):
    return dict["num"]

def print_report(word_length, expanded_dictionary_array):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_length} words found in the document")
    print("")
    for entry in expanded_dictionary_array:
            print(f"The '{entry['char']}' character was found {entry['num']} times")

    print("--- End report ---")

main()
