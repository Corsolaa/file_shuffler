import os

def start_program():
    shuffle_directory = select_directory()

def select_directory():
    while True:
        print("Please input the directory where to files are located,")
        shuffle_directory = input(" that you want to shuffle: ")
        if os.path.isdir(shuffle_directory):
            break
        print("Please enter a valid directory...")
    print("Are you sure you want to shuffle: " + shuffle_directory)
    question = input("Please enter Y(es) or N(o): ")
    return shuffle_directory

def yes_or_no_filter(question):
    


if __name__ == '__main__':
    start_program()
