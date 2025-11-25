print("PythonGenie: Hello! I am PythonGenie. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    user_input = user_input.strip().lower()

    if user_input in ["bye", "exit", "quit"]:
        print("PythonGenie: Goodbye! Have a magical day ✨")
        break

    elif user_input in ["hi", "hello", "hey"]:
        print("PythonGenie: Hello! How can I assist you today?")

    elif "your name" in user_input:
        print("PythonGenie: I'm PythonGenie, your friendly rule-based chatbot.")

    elif "help" in user_input or "options" in user_input:
        print("PythonGenie: I can respond to greetings, internship questions, course info, and more.")
        print("PythonGenie: Try asking things like 'internship info', 'what courses', or 'time'.")

    elif "course" in user_input or "courses" in user_input:
        print("PythonGenie: This internship mainly focuses on Python and basic data analysis.")

    elif "internship" in user_input:
        print("PythonGenie: You are doing the Python Developer internship. This is Task 8: Chatbot! 🧠")

    elif "time" in user_input:
        print("PythonGenie: I cannot show the current time yet, but please check your system clock ⏰.")

    elif "thank" in user_input:
        print("PythonGenie: You're most welcome! ✨")

    else:
        print("PythonGenie: Sorry, I didn't understand that. Type 'help' to see what I can do.")
