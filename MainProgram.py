import time

text_file = "word-service.txt"

def WriteToTextFile(file, content):
    print("Writing to file...")
    with open(file,"w") as file_opened:
        file_opened.write(content)

def ListenToTextFile(file, content):
    print("Listening to file for changes...")
    while True:
        time.sleep(2)   # leave this sleep in to avoid permission errors
                        # (from both files trying to read/write at the same time)
        with open(file, "r") as file_opened:
            read_text = file_opened.read()
        if read_text.lower() == "stop":
            return "stop"
        elif read_text != content:
            print("Received words!")
            return read_text

if __name__ == "__main__":
    # when you want to stop using the service, write "stop" to the file. (any case is fine "STOP", "Stop" etc.)
    received_text = ""
    while True:
        print("\nReady to receive request...")
        print('When you want to stop using the service, enter "stop".')
        content = input ("Please enter many words you want to receive: ")
        print()
        WriteToTextFile(text_file, content)
        received_text = ListenToTextFile(text_file, content)
        if received_text == "stop":
            WriteToTextFile(text_file, "")
            print("\nStopping MainProgram - Thanks for playing!")
            break
        WriteToTextFile(text_file, "")
        print("Now you can do other things with these words:\n"+ received_text)



