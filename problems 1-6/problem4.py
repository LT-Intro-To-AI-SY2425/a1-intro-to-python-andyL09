# ### 4. **Simple AI: Chatbot**:
#    - Create a basic chatbot using `if` and `else` statements.
#        The program should take input from the user and respond 
#        to simple keywords like "hello", "bye", or "how are you?". 
#        You can expand this with more responses as you get comfortable.

print# Simple chatbot using if-else statements

def chatbot():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easier matching

        if "hello" in user_input:
            print("Chatbot: Hi there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but thanks for asking!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the loop
        else:
            print("Chatbot: I don't understand that. Try saying something else.")

# Run the chatbot
chatbot()
