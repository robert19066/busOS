import os
import subprocess

def display_menu():
    print("\nB.U.S Command-Line Text Editor")
    print("1. Open file")
    print("2. Save file")
    print("3. Edit text")
    print("4. Exit")

def open_file():
    file_name = input("Enter the file name to open: ")
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)
            return content, file_name
    else:
        print("File not found.")
        return "", file_name

def save_file(content, file_name):
    if file_name == "":
        file_name = input("Enter the file name to save as: ")
    with open(file_name, 'w') as file:
        file.write(content)
    print("File saved successfully.")

def edit_text():
    file_name = input("Enter the file name to edit: ")
    content = ""
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
        print("\n--- Editing Mode ---")
        print("Current content:")
        print(content)
        print("Type your text below (type 'SAVE' on a new line to save and exit):")
        new_content = ""
        while True:
            line = input()
            if line == "SAVE":
                break
            new_content += line + '\n'
        save_file(new_content, file_name)
    else:
        print("File not found.")

def main():
    os.system('cls')
    content = ""
    file_name = ""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            content, file_name = open_file()
        elif choice == '2':
            save_file(content, file_name)
        elif choice == '3':
            edit_text()
        elif choice == '4':
            print("Exiting B.U.S Text Editor. Goodbye!")
            subprocess.run(["python", "C:/Users/Lenovo/Desktop/busOS/core/comand.py"])
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
