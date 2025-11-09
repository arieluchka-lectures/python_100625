import banana
import greet_goodbye
# from greet_goodbye import DEFAULT_USER_NAME



banana.hello_user()

greet_goodbye.hello_user()

def ask_for_name(username=greet_goodbye.DEFAULT_USER_NAME):
    print(f"Great to meet you {username}!")



if __name__ == '__main__':
    greet_goodbye.hello_user()
    banana.bananas()

    ask_for_name()
    banana.bananas()


    greet_goodbye.goodbye_user()
    banana.bananas()
