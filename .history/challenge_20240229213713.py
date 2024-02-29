# Little Sister’s Vocabulary
# https://exercism.org/tracks/python/exercises/little-sisters-vocab

# Instructions: You are helping your younger sister with her English vocabulary homework,
# which she is finding very tedious. Her class is learning to create new words by adding
# prefixes and suffixes. Given a set of words, the teacher is looking for correctly transformed
# words with correct spelling by adding the prefix to the beginning or the suffix to the ending.
# There's four activities in the assignment, each with a set of text or words to work with.

# Task 1
print("1. Add a prefix to a word -->")

def add_prefix_to_word():
    word_list  = ('''
        happy
        manageable
    ''')
    print(word_list )

    # while loop for Error Handling - Invalid inputs
    while True:
        word = input("Please select a word from the list to add the prefix 'un-': ").lower()  # .lower() for Error Handling - Incorrect capitalization

        if word in word_list :
            print("Your selected word:", word)
            break
        else:
            print("Invalid option. Please choose a word from the provided list.")

    # adding 'un-' to selected word by concatenated str with '+'
    prefix = "un"
    add_prefix_un = prefix + word
    print("Your selected word with un- prefix:", add_prefix_un)

# Call the function to execute
add_prefix_to_word()

# Task 2
print("\n2. Add prefixes to word groups -->")

def add_prefix_to_groups():
    def add_prefix(group, prefix):
        return f" :: {prefix}".join(group)
    # separate words with '::' and add first word from a group to the rest of words beginnings using .join()
    make_word_groups1 = ['en', 'close', 'joy', 'lighten']
    new_set1 = (' :: en'.join(make_word_groups1))
    print("\nFirst group:", make_word_groups1)
    print("With prefix", new_set1)

    make_word_groups2 = ['pre', 'serve', 'dispose', 'position']
    new_set2 = (' :: pre'.join(make_word_groups2))
    print("\nSecond group:", make_word_groups2)
    print("With prefix", new_set2)

    make_word_groups3 = ['auto', 'didactic', 'graph', 'mate']
    new_set3 = (' :: auto'.join(make_word_groups3))
    print("\nThird group:", make_word_groups3)
    print("With prefix", new_set3)

    make_word_groups4 = ['inter', 'twine', 'connected', 'dependent']
    new_set4 = (' :: inter'.join(make_word_groups4))
    print("\nFourth group:", make_word_groups4)
    print("With prefix", new_set4, "\n")

# Call the function to execute
add_prefix_to_groups()

# Task 3
print("3. Remove a suffix from a word -->")

def remove_suffix_from_word():
    first = ('''
        heaviness
        sadness
    ''')
    print(first)

    # while loop for Error Handling - Invalid inputs
    while True:
        choose = input("Please choose a word from the 2 word list you want to remove '-ness': ").lower()  # .lower() for Error Handling - Incorrect capitalization

        if choose in first:
            print("You choose:", choose)
            break
        else:
            print("Invalid option. Please choose a word from the provided list.")

    # remove 4 last letters
    remove_suffix_ness = choose[:-4]
    # print(remove_suffix_ness)         # test print

    # checking if the word is ending in 'i'
    if remove_suffix_ness[-1] == 'i':
        # removing last letter 'i' and replacing with 'y'
        print("After removing '-ness' and changing last letter:", remove_suffix_ness[:-1] + "y", "\n")
    else:
        # if word doesn't end with 'i' print the output
        print("After removing '-ness':", remove_suffix_ness, "\n")

# Call the function to execute
remove_suffix_from_word()

# Task 4
print("4. Extract and transform a word -->\n")

adjective_to_verb1 = "I need to make that bright."
# split sentence to substrings with .split(). Will split the string on whitespace
adjective_to_verb1.split()

print("First split sentence:", adjective_to_verb1.split())
# selecting last word, removing '.' and adding 'en' to the end
print("Extracted and transformed last word:", adjective_to_verb1.split()[-1].strip(".") + "en")

adjective_to_verb2 = "It got dark as the sun set."
# split sentence to substrings with .split(). Will split the string on whitespace
adjective_to_verb2.split()

print("\nSecond split sentence:", adjective_to_verb2.split())
# selecting third word and adding 'en' to the end
print("Extracted and transformed 3rd word:", adjective_to_verb2.split()[2] + "en")
