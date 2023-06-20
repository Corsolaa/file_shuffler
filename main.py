import os


def start_program():
    selected_dir = select_directory()
    if selected_dir[0]:
        shuffle_directory(selected_dir[1])


def select_directory():
    while True:
        print("Please input the directory where to files are located,")
        selected_dir = input("that you want to shuffle: ")
        if os.path.isdir(selected_dir):
            break
        print("Please enter a valid path to a dictionary...")
    print("Are you sure you want to shuffle: " + selected_dir)
    input_counter = 0
    while True:
        input_counter += 1
        question = input("Please enter yes or no: ")
        if question.lower() == "yes":
            return [True, selected_dir]
        elif question.lower() == "no":
            return [False, ""]
        if input_counter == 3:
            print("then go away")
            return [False, ""]


def shuffle_directory(dir_path):
    counter = 0
    index = 1
    for path in os.listdir(dir_path):
        print("[" + str(index) + " - " + str(len(os.listdir(dir_path))) + "]")
        extention = path.split(".")[-1]
        old_path = dir_path + "/" + path
        new_path = dir_path + "/" + "piemelsaus_img_" + str(counter) + "." + extention
        already_there = ""
        while True:
            if os.path.exists(new_path):
                already_there = already_there + "."
                counter += 1
                new_path = dir_path + "/" + "piemelsaus_img_" + str(counter) + "." + extention
            else:
                if already_there != "":
                    print("times file name changed:" + already_there)
                break
        counter += 1
        index += 1
        os.rename(old_path, new_path)


if __name__ == '__main__':
    start_program()
