import time
import subprocess
import sys
import os
import google.generativeai as genai

stop = True  # Initialize the loop control variable

key = "AIzaSyDU4toaHTSxrtET3MR_O00HBaWNOqoLUoA"
genai.configure(api_key=key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

def getver():
    print("""
 ____  _    _ ____   ____  ____   ____   _____ 
| __ )| |  | | __ ) / ___||  _ \ / ___| |_   _|
|  _ \| |  | |  _ \ \___ \| |_) | |  _    | |  
| |_) | |__| | |_) | ___) |  __/| |_| |   | |  
|____/ \____/|____/ |____/|_|    \____|   |_|  
                                            
  B.U.S OS - The Basic Ultra Small OS
    
Version:1.0 BETA STABILE           
""")

def gethelp():
    print("""
    getver: Shows your B.U.S OS version 
    strbeep (BETA): Opens the BEEP text editor editor.
    stop: Stops the B.U.S OS session.
    strAI (BETA): Starts an instance of HelperAI (you can come back to P.L.P only if you restart).
    gethelp: Shows all commands.
    clscr: Clears the screen.
    getfiles: shows all files in the "user" directory
    strguide: shows the basic busOS guide
    more soon!
""")

def list_files_in_folder(folder_path):
    try:
        # List all files and directories in the specified folder
        items = os.listdir(folder_path)
        
        # Filter out directories, keeping only files
        files = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]
        
        # Print out the files
        print(f"Files in folder '{folder_path}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The folder '{folder_path}' was not found.")
    except PermissionError:
        print(f"Permission denied to access the folder '{folder_path}'.")

def strguide():
    print("""
            Editing,Creating or Saving(with another extension) text files:
                1.type the comand strbeep(to start the beep text editor)
                2.select the desired option
            Shutdown:
                1.type the comand "stop" into the P.L.P.
            Creating an instance of HelperAI
                1.type strAI in the P.L.P
                2.enjoy(note that you need to exit to go back to the P.L.P!)
            Clearing screen
                1.type "slscr" in the P.L.P
          """)

def strbeep():
    subprocess.run(["python", "C:/Users/Lenovo/Desktop/busOS/core/beep.py"])

def stop():
    os.system('cls')
    print("Exiting B.U.S OS session...")
    time.sleep(2)
    sys.exit()

def helpme():
    global stop  # Make sure to reference the global stop variable
    stop = False
    os.system('cls')
    while True:
        user_input = str(input("busOS_1.0$tag=HelperAI//_user#:"))
        print(chat_with_gemini(user_input))

def clscr():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

os.system('cls')
time.sleep(1.3)
print("""
B.U.S OS Command Line Prompt (P.L.P)
Type "gethelp" for list of commands
""")

while stop:
    user_input = str(input("busOSh$_user#:"))
    if user_input == "getver":
        getver()
    elif user_input == "strbeep":
        strbeep()
    elif user_input == "stop":
        stop()
    elif user_input == "strAI":
        helpme()
    elif user_input == "gethelp":
        gethelp()
    elif user_input == "clscr":
        clscr()
    elif user_input == "getfiles":
        path = input("Path to folder:")
        list_files_in_folder(path)
    elif user_input == "strguide":
        strguide()
    else:
        print(f"No command exists named {user_input}! Check spelling!")
