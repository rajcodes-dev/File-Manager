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


def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Exit")

        choice = int(input("Enter you choice(1-6): ").strip())

        if choice == 1:
            filename = input("Enter filename to create.").strip()
            create_file(filename)

        elif choice == 2:
            view_all_files()

        elif choice == 3:
            filename = input("Enter the filename you want to delete.").strip()
            delete_file(filename)

        elif choice == 4:
            filename = input("Enter the filename to read.")
            read_file(filename)
        
        elif choice == 5:
            filename = input("Enter the filename to edit.")
            edit_file(filename)
        
        elif choice == 6:
            print("Exiting App......")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
