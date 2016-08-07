import os
import random


def random_number_maker(i):
    """
    input: random number
    output: int type one hundred time of random number
    """
    return int(i * 100)


def encryption_files(file_list, target_dir):
    os.chdir(target_dir)
    for file_name in file_list:
        random_number = random_number_maker(random.random())
        number_added_files = "{0}{1}".format(random_number, file_name)
        print("Old Name - " + file_name)
        print("New Name - " + number_added_files)
        os.rename(file_name, number_added_files)


def decryption_files(file_list, target_dir):
    saved_path = os.getcwd()
    print saved_path
    os.chdir(target_dir)
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print file_name


def user_interface():
    """
    user interface
    """
    file_list = os.listdir("/Users/macpro/Google Drive/code/project03/message")
    target_dir = "/Users/macpro/Google Drive/code/project03/message"
    print file_list
    print target_dir
    while True:
        os.system('clear')
        print("Select what you want 1. encryption, 2. decryption 3. exit")
        choice = raw_input("Number : ")
        if choice == '1':
            encryption_files(file_list, target_dir)
            break
        elif choice == '2':
            decryption_files(file_list, target_dir)
            break
        elif choice == '3':
            break
        else:
            print "Type again"


# run

user_interface()
