print("Bot: Hi! I am a very simple chatbot.")
print("Bot: You can say hi, tell me your name, or say bye.")

name = ""

while True:
    user_input = input("You: ").lower() 

    if user_input == "hi" or user_input == "hello" or user_input == "hey":
        print("Bot: Hello!")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user_input.startswith("my name is"):
        name = user_input.replace("my name is", "").strip().capitalize()
        print("Bot: Nice to meet you,", name)

    elif user_input == "what is my name":
        if name == "":
            print("Bot: You haven't told me your name yet.")
        else:
            print("Bot: Your name is", name)

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand. Please try again.")
