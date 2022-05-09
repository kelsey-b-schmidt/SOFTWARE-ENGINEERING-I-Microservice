PseudoRandom Word Generator is a program designed to communicate via text files, to generate a list of random words, 
to be used in some other program.

## Installation

You will need to have Python and the package manager [pip](https://pip.pypa.io/en/stable/) installed.

Open a terminal, cd into the "Microservice" folder, 
and use pip to install the requirements with the following command:

```bash
pip install -r requirements.txt
```
Once the dependencies are installed, from the terminal, start the Microservice by entering:
```bash
python Microservice.py
```
## Usage

You may edit the text file variable to the text file of your choice. 

Be careful with the file path if traveling between folders!

```python
# edit the text file variable to the text file of your choice
text_file = "word-service.txt"
```
A sample file has been provided, as well as a sample program which can be used to demonstrate a call to this 
Microservice. To see the program in action, AFTER starting the Microservice, in a separate terminal, cd into the 
"Microservice" folder again, and enter the command: 
```bash
python MainProgram.py
```
To stop sending/receiving input to/from the MainProgram.py file, enter "stop" when prompted. This can be any case, 
so "STOP", "Stop", etc., are fine.

To stop sending/receiving input to/from the Microservice.py file, write "stop" to the text file, either through your 
program or manually. Otherwise, you may need to terminate the process that is running it.

Sample print statements have been provided for debugging purposes. 
They can be commented out by adding "#" before the line.

## License
[MIT](https://choosealicense.com/licenses/mit/)