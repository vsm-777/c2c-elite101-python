
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
    print("Welcome to the FinWiz chatbot! ")
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}! Let's see how we can help you today.")
    age=int(input(f"How old are you, {name}? "))
    return age

def additional_info():
    college=input("Are you currently attending college? (yes/no)").lower()
    try:
        credit_score=int(input("What is your current credit score? (300-850) "))
        if credit_score<300 or credit_score>850 or not isinstance(credit_score,int):
            print("Invalid credit score. Please enter a number between 300 and 850.")
            return additional_info()
    except ValueError:
        print("Invalid input. Please enter a numeric value for credit score.")
        return additional_info()
    print("What is your financial goal?")
    print("1. Saving money")
    print("2. Building credit")
    print("3. Managing everyday spending")
    print("4. Growing my business")
    print("5. If none of the above")
    goal=input("Please select the number corresponding to your financial goal: ")
    if goal not in ['1','2','3','4','5']:
        print("Invalid choice. Please select a valid option.")
        return additional_info()
    return college,credit_score,goal

def additional_info_someone_else():
    college=input("Are they currently attending college? (yes/no)").lower()
    try:
        credit_score=int(input("What is your current credit score? (300-850) "))
        if credit_score<300 or credit_score>850 or not isinstance(credit_score,int):
            print("Invalid credit score. Please enter a number between 300 and 850.")
            return additional_info_someone_else()
    except ValueError:
        print("Invalid input. Please enter a numeric value for credit score.")
        return additional_info_someone_else()
    print("What is their financial goal?")
    print("1. Saving money")
    print("2. Building credit")
    print("3. Managing everyday spending")
    print("4. Growing my business")
    goal=input("Please select the number corresponding to your financial goal: ")
    if goal not in ['1','2','3','4']:
        print("Invalid choice. Please select a valid option.")
        return additional_info_someone_else()
    return college,credit_score,goal

def book_appointment():
    print("\n Let's book an appointment for you to speak with a financial advisor.")
    print("Please choose a day for your appointment:")
    print("1. Monday")
    print("2. Tuesday")
    print("3. Wednesday")
    print("4. Thursday")
    print("5. Friday")
    day_choice = input("Enter the number corresponding to your preferred day: ")
    days = {'1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday'}
    if day_choice not in days:
        print("Invalid choice. Please select a valid option.")
        return book_appointment()
    else:
        print(f"Your appointment has been booked for {days[day_choice]}. A financial advisor will reach out to you soon.\n")
    print("Thank you for using the FinWiz chatbot. Goodbye!")
    exit()

def recommendations(age,college,credit_score,goal):
    print("\nBased on the information you provided, here is what we recommend:")
    recommendation=""

    if age<18:
        recommendation="Youth Savings Account - This will alway you to start saving your money even as a minor!"
    elif college=="yes" and age<=25:
        recommendation="Student Checking Account - Designed for college students with no monthly fees and ATM access."
    elif goal=="1":
        recommendation="High-Yield Savings Account - To help you grow your savings faster with better interest rates."
    elif goal=="2" and credit_score<650:
        recommendation="Secured Credit Card - A great way to build or rebuild your credit with responsible use."
    elif goal =='2' and credit_score>=650:
        recommendation="Rewards Credit Card - Earn points or cash back on your everyday purchases."
    elif goal=='3':
        recommendation="Everyday Checking Account - For managing your daily expenses with ease."
    elif goal=='4':
        recommendation="Business Checking Account - Tailored for small business owners with features to manage finances."
    else:
        recommendation="Please book an appointment for personalized financial advice."

    print("Recommendation: " + recommendation + "\n")
    if "book an appointment" in recommendation:
        book_appointment()
    return recommendation

def show_setup_steps(account_type):
    print("Here are the steps to set up your recommended account:")
    if "Youth Savings Account" in account_type:
        print("1. Provide a parent or guardian's information.")
        print("2. Submit identification documents.")
        print("3. Make an initial deposit.")
    elif "Student Checking Account" in account_type:
        print("1. Provide proof of student status.")
        print("2. Submit identification documents.")
        print("3. Make an initial deposit.")
    elif "High-Yield Savings Account" in account_type:
        print("1. Submit identification documents.")
        print("2. Make an initial deposit.")
    elif "Secured Credit Card" in account_type or "Rewards Credit Card" in account_type:
        print("1. Submit identification documents.")
        print("2. Provide income information.")
        print("3. Make a security deposit (for secured cards).")
    elif "Everyday Checking Account" in account_type:
        print("1. Submit identification documents.")
        print("2. Make an initial deposit.")
    elif "Business Checking Account" in account_type:
        print("1. Provide business documentation.")
        print("2. Submit identification documents.")
        print("3. Make an initial deposit.")
    print("\nOnce you have completed these steps, your account will be up and running!")
    print()

def create_account_for_someone_else():
    print("You are creating an account for someone else. Please provide their details.")
    name = input("Enter the person's name: ")
    age = int(input("Enter their age: "))
    college,credit_score,goal=additional_info_someone_else()
    account_type=recommendations(age,college,credit_score,goal)
    show_setup_steps(account_type)

def options(name):
    print(f"How can I help you {name}?")
    print("1. Learn about different account types")
    print("2. Get a personalized recommendation")
    print("3. Create an account for someone else")
    print("4. Exit the conversation")
    print()
    return input("Which option would you like to choose? ")

def show_account_types():
    print("\nHere are some common account types we offer:")
    print("1. Savings Account - A safe place to store your money and earn interest.")
    print("2. Checking Account - For everyday transactions and bill payments.")
    print("3. Credit Card - To help build credit and manage expenses.")
    print("4. Business Account - Tailored for business owners to manage finances.")
    print("5. Student Account - Designed for students with special benefits.")
    print()



def user_choice(name,choice,age):
    while choice != '4':
        if choice == '1':
            show_account_types()
        elif choice == '2':
            college,credit_score,goal=additional_info()
            account_type=recommendations(age,college,credit_score,goal)
            show_setup_steps(account_type)
        elif choice == '3':
            create_account_for_someone_else()
        else:
            print("Invalid choice. Please select a valid option.\n")

        choice = options(name)
    print("Exiting the conversation. Goodbye!")



def main():
    user_name = get_user_name()
    age=greet_user(user_name)
    choice=options(user_name)
    user_choice(user_name,choice,age)

if __name__ == "__main__":
    main()
