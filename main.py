
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_name():
    print("Welcome to our store's chatbot! ")
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}, how are you?")
    return input(f"How old are you, {name}? ")

def options(name):
    print(f"How can I help you {name}?")
    print("1. Placeholder option 1")
    print("2. Placeholder option 2")
    print("3. Placeholder option 3")
    print("4. Exit the conversation")
    print()
    return input("Which option would you like to choose? ")

def user_choice(choice):
    while choice != '4':
        if choice == '1':
            print("You selected option 1.")
        elif choice == '2':
            print("You selected option 2.")
        elif choice == '3':
            print("You selected option 3.")
        elif choice == '4':
            print("Exiting the conversation. Goodbye!")
        else:
            print("Invalid choice. Please select a valid option.")



def main():
    user_name = get_user_name()
    age=greet_user(user_name)
    choice=options(user_name)

if __name__ == "__main__":
    main()
