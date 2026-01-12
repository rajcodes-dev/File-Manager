import os


def create_file(filename):
    try:
        with open(filename, "x") as f:
            print(f"File name {filename}: Created successfully!")
    except FileExistsError:
        print(f"File name {filename}: It already exists!")
    except Exception as e:
        print("An error occured!")


def view_all_files():
    files = os.listdir()
    if not files:
        print("There is no file.")
    else:
        print("Files are in the directory!")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} is deleted successfully!")
    except FileExistsError:
        print(f"File name {filename}: It already exists!")
    except Exception as e:
        print("An error occured!")


def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"Content of {filename}: \n{content}")
    except FileExistsError:
        print(f"File name {filename}: It already exists!")
    except Exception as e:
        print("An error occured!")


def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter the content you want to add.")
            f.write(content + "\n")
            print(f"{filename} is edited.")
    except FileExistsError:
        print(f"File name {filename}: It already exists!")
    except Exception as e:
        print("An error occured!")



