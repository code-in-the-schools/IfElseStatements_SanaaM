userInput = str(input("Enter a phrase..."))
newInput = userInput.lower()
print(newInput)

vowels = ["a", "e", "i", "o", "u"]
for i in newInput:
  if i in vowels: 
    print (i + "is a vowel")
else:
      print(i + "is a consonant")