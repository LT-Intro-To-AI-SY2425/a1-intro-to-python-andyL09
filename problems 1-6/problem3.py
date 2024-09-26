# ### 3. **Palindrome Checker**:
#    - Write a Python program that takes a word as input 
#       and checks if it is a palindrome (a word that reads the 
#       same backward as forward).

def reverse(string):
    string = string[::-1]
    return string

userWord = input("enter a word to check if its a palindrome")

flippedUserWord = reverse(userWord)

if userWord == flippedUserWord:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")