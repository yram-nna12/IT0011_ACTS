text = input("Enter a string: ")

vowels = consonants = spaces = others = 0


vowel_set = "AEIOUaeiou"

for char in text:
    if char.isalpha(): 
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
    elif char.isspace():  
        spaces += 1
    else:
        others += 1


print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
print("Other characters:", others)
