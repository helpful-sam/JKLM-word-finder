import pyperclip
import random
import os

while True:
    
    string = input("Chunk [stop program]: ")

    if string == "stop program":
        break
    elif not(string.isalpha()):
        continue

    current_directory = os.path.dirname(os.path.abspath(__file__))
    dictionary = os.path.join(current_directory, '..', 'assets', 'dictionary.txt')

    with open(dictionary) as f:
        lines = f.readlines()

    # Filter the words that contain the search string and store them in a list
    words = [word for line in lines for word in line.split() if string in word]

    if len(words) == 0:
        continue

    # sort the words in decreasing order of length
    sorted_words = sorted(words, key=len, reverse=True)

    # copy a random word to the clipboard
    random_word = sorted_words[(0 + random.randint(0, len(sorted_words))) % len(sorted_words)]
    pyperclip.copy(random_word)
    
    # Print the longest word
    print(random_word)
    print("")

    # Print out the words in a 4-column table
    '''
    counter = 0
    for word in sorted_words:
        print(word, end=" "*(15-len(word)))
        counter += 1
        if counter % 5 == 0:
            print()
    print("")
    '''