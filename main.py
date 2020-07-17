userInput = str(input("Enter a phrase..."))
newInput = userInput.lower()
print(newInput)

vowels = ["a", "e", "i", "o","u"]
numberVowels = 0 
numberConsonants = 0 
for i in newInput: 
  if i in vowels: #check the vowel list 
    print(i + " is a vowel")
  numberVowels = numberVowels + 1 
else: 
    print(i + " is a consonant")
    numberConsonants = numberConsonants + 1 
    print("# of vowels:" + str(numberVowels))
    print("# of consonants:" + str(numberConsonants))