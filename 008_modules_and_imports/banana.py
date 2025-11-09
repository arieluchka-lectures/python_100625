from some_common_functions import my_funcs
# from FOLDER.FOLDER.FOLDER import FILE
# from FOLDER.FOLDER.FOLDER.FILE import SPECIFIC_OBJECT

from some_common_functions.my_funcs import is_even



def bananas():
    print("i like bananas in my milkshake")


def hello_user():
    print("Greetings banana lover user! Welcome to the code!")



def is_good_amount_of_bananas(num_of_bananas: int):
    if 10 <= num_of_bananas < 100:
        if is_even(num_of_bananas):
            print("good number of bananas! monke like :)")








if __name__ == '__main__':
    first_bananas = int(input("how many bananas you have?"))

    is_good_amount_of_bananas(first_bananas)

    second_bananas = int(input("how many bananas you have?"))
    is_good_amount_of_bananas(second_bananas)










    #
    #
    #
    is_good_amount_of_bananas(num_of_bananas=15)
    is_good_amount_of_bananas(num_of_bananas=16)
    is_good_amount_of_bananas(num_of_bananas=5)
    is_good_amount_of_bananas(num_of_bananas=67)