

print("Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

  
    if user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a nice day!")
        break

  
    elif user_input in ["hi", "hello", "hey"]:
        print("Chatbot: Hello! How can I help you?")

   
    elif "your name" in user_input:
        print("Chatbot: I am a simple rule-based chatbot created using Python.")

   
    elif "weather" in user_input:
        print("Chatbot: I can't check weather now, but I hope it's nice where you are!")

   
    elif "time" in user_input:
        print("Chatbot: I can't tell the time yet, but you can check your device clock!")

    
    elif "how are you" in user_input:
        print("Chatbot: I am just a program, but I'm running great! 😊 What about you?")

    
    else:
        print("Chatbot: Sorry, I don't understand that. Can you try asking something else?")

