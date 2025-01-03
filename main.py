def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")

def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()
