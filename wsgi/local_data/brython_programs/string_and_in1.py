print(3 in [1, 2, 3])
print("3" in [1, 2, 3])
print("3" in [1, 2, "3"])
VOWELS = ['a', 'e', 'i', 'o', 'u']
def is_a_vowel(c):
    # check if c is a vowel
    lowercase_c = c.lower()
    if lowercase_c in VOWELS:
        # Return (BOOLEAN!) True if c is a vowel
        return True
    else:
        # c must not be a vowel; return (BOOLEAN!) False
        return False
        
def only_vowels(phrase):
    # Takes a phrase, and returns a string of all the vowels
    # Initalize an empty string to hold all of the vowels
    vowel_string = ''
    for letter in phrase:
        # check if each letter is a vowel
        if is_a_vowel(letter):
            # If it's a vowel, we append the letter to the vowel string
            vowel_string = vowel_string + letter
            # if not a vowel, we don't care about it- so do nothing!
    return vowel_string
    # Code after a "return" doesn't print
    print("A line of code after the return!")
print(only_vowels("Takes a phrase, and returns a string of all the vowels"))