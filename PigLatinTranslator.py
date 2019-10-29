
def pig_latin_translator():
    phrase = input("Enter the phrase that you would like to be translated here: ")
    phrase_array = phrase.split()
    new_phrase = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in phrase_array:
        if not word.isalpha(): # checks if the phrase only contains letters
            print("\nMake sure your phrase only contains letters, not numbers or special characters\n")
            pig_latin_translator()
            return

        word = word.lower()

        # checks if the first letter is a vowel
        if word[0] in vowels:
            new_phrase.append(word + "-yay")

        # checks if the word has more than two letters, and the first two letters are consonants and the third is a 'y'
        elif len(word) > 2 and (word[0] not in vowels and word[1] not in vowels and word[2] == "y"):
            new_phrase.append(word[2:] + "-" + word[0] + word[1] + "ay")

        # checks if the word has more than one letter, and the first two letters are consonants and the second is not a 'y'
        elif len(word) > 1 and (word[0] not in vowels and word[1] not in vowels and word[1] != "y"):
            new_phrase.append(word[2:] + "-" + word[0] + word[1] + "ay")

        # checks if the first letter is a consonant
        elif word[0] not in vowels:
            new_phrase.append(word[1:] + "-" + word[0] + "ay")

    print("\nTranslated phrase:", end=" ")
    for new_word in new_phrase:
        print(new_word, end=" ")


print("\nWelcome to the Pig Latin translator!\n")
pig_latin_translator()



