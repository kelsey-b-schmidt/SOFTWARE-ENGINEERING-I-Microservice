import time
from random_word import RandomWords

r = RandomWords()
text_file = "word-service.txt"

def WriteToTextFile(file, number):
    print("Writing to file...")
    limit = int(number)
    words = r.get_random_words(limit=number)
    with open(file, "w") as file_opened:
        file_opened.write(str(words))

def ListenToTextFile(file, content):
    while True:
        time.sleep(5)   # leave this sleep in to avoid permission errors
                        # (from both files trying to read/write at the same time)
        with open(file, "r") as file_opened:
            read_text = file_opened.read()
        if read_text != "" and read_text != content:
            if read_text.lower() == "stop":
                return "stop"
            print('\nRequest received...')
            return read_text

if __name__ == "__main__":
    content = ""
    while True:
        content = ListenToTextFile(text_file, content)
        if content == "stop":
            print("\nStopping Microservice - Thanks for playing!")
            break
        WriteToTextFile(text_file, content)
        print("Ready to receive another request...")


