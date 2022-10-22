print("Hey, do you wanna see a cool trick I can do? I can count how many letters in a list of letters are uppercase!")
print("Here, I can prove it!")
print("Gimme a list of letters!")

letter = input("Enter a list of letters, seperating each by a comma. (put both uppercase and lowercase!) ")
letter_list = letter.split(",")
print("The list you gave was...")
print(letter_list)
print("And if we seperate those, we get...")
for letter in letter_list:
    print(letter)
    
print("Now, I'm going to count how many of those are uppercase!")

capital = 0
for letter in letter_list:
    print(letter)
    if letter.isupper() == True:
        capital = capital + 1

print(capital)