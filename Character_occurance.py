word = input("Enter your own word:")
character = input("Enter a character:")
i = 0
count = 0
while i<len(word):
    if word[i]==character:
        count = count + 1
    i = i + 1
print("The total number of word the character is coming", count)