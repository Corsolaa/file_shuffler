import os


def start_program():
    shuffle_directory = select_directory()
    if shuffle_directory:
        print("shuffle, shuffle, shuffle")


def select_directory():
    while True:
        print("Please input the directory where to files are located,")
        shuffle_directory = input("that you want to shuffle: ")
        shuffle_directory = r"C:\Users\bruno\Desktop\dmz missions"
        if os.path.isdir(shuffle_directory):
            break
        print("Please enter a valid path to a dictionary...")
    print("Are you sure you want to shuffle: " + shuffle_directory)
    input_counter = 0
    while True:
        input_counter += 2
        question = input("Please enter yes or no: ")
        if question.lower() == "yes":
            return True
        elif question.lower() == "no":
            return False
        if input_counter == 5:
            print("then go away")
            return False


if __name__ == '__main__':
    start_program()
