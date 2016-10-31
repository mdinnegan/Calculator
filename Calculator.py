#importing
import Myro
from Myro import *

#defining variables
N1 = 1
N2 = N1 + 1
N3 = N2 + 1
N4 = N3 + 1
N5 = N4 + 1
N6 = N5 + 1
N7 = N6 + 1
N8 = N7 + 1
N9 = N8 + 1

#addition function
def addition():
    answer1 = askQuestion("First number?", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    answer2 = askQuestion("Second number?", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    if answer1 == "1":
        X = N1
    if answer1 == "2":
        X = N2
    if answer1 == "3":
        X = N3
    if answer1 == "4":
        X = N4
    if answer1 == "5":
        X = N5
    if answer1 == "6":
        X = N6
    if answer1 == "7":
        X = N7
    if answer1 == "8":
        X = N8
    if answer1 == "9":
        X = N9

    if answer2 == "1":
        Y = N1
    if answer2 == "2":
        Y = N2
    if answer2 == "3":
        Y = N3
    if answer2 == "4":
        Y = N4
    if answer2 == "5":
        Y = N5
    if answer2 == "6":
        Y = N6
    if answer2 == "7":
        Y = N7
    if answer2 == "8":
        Y = N8
    if answer2 == "9":
        Y = N9
    
    print(X + Y)

#subtraction function
def subtraction():
    answer1 = askQuestion("First number?", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    answer2 = askQuestion("Second number?", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    if answer1 == "1":
        X = N1
    if answer1 == "2":
        X = N2
    if answer1 == "3":
        X = N3
    if answer1 == "4":
        X = N4
    if answer1 == "5":
        X = N5
    if answer1 == "6":
        X = N6
    if answer1 == "7":
        X = N7
    if answer1 == "8":
        X = N8
    if answer1 == "9":
        X = N9

    if answer2 == "1":
        Y = N1
    if answer2 == "2":
        Y = N2
    if answer2 == "3":
        Y = N3
    if answer2 == "4":
        Y = N4
    if answer2 == "5":
        Y = N5
    if answer2 == "6":
        Y = N6
    if answer2 == "7":
        Y = N7
    if answer2 == "8":
        Y = N8
    if answer2 == "9":
        Y = N9
    
    print(X - Y)   

#multiplication function
def multiplication():
    answer1 = askQuestion("First number?", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    answer2 = askQuestion("Second number?", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    if answer1 == "1":
        X = N1
    if answer1 == "2":
        X = N2
    if answer1 == "3":
        X = N3
    if answer1 == "4":
        X = N4
    if answer1 == "5":
        X = N5
    if answer1 == "6":
        X = N6
    if answer1 == "7":
        X = N7
    if answer1 == "8":
        X = N8
    if answer1 == "9":
        X = N9

    if answer2 == "1":
        Y = N1
    if answer2 == "2":
        Y = N2
    if answer2 == "3":
        Y = N3
    if answer2 == "4":
        Y = N4
    if answer2 == "5":
        Y = N5
    if answer2 == "6":
        Y = N6
    if answer2 == "7":
        Y = N7
    if answer2 == "8":
        Y = N8
    if answer2 == "9":
        Y = N9
    
    print(X * Y)

#division function
def division():
    answer1 = askQuestion("First number?", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    answer2 = askQuestion("Second number?", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    if answer1 == "1":
        X = N1
    if answer1 == "2":
        X = N2
    if answer1 == "3":
        X = N3
    if answer1 == "4":
        X = N4
    if answer1 == "5":
        X = N5
    if answer1 == "6":
        X = N6
    if answer1 == "7":
        X = N7
    if answer1 == "8":
        X = N8
    if answer1 == "9":
        X = N9

    if answer2 == "1":
        Y = N1
    if answer2 == "2":
        Y = N2
    if answer2 == "3":
        Y = N3
    if answer2 == "4":
        Y = N4
    if answer2 == "5":
        Y = N5
    if answer2 == "6":
        Y = N6
    if answer2 == "7":
        Y = N7
    if answer2 == "8":
        Y = N8
    if answer2 == "9":
        Y = N9
    
    print(X / Y)            

#question interactive function
def askoperation():
    answer = askQuestion("Which operation?", ["addition", "subtraction", "multiplication", "division"])
    if answer == "addition":
        addition()
    if answer == "subtraction":
        subtraction()
    if answer == "multiplication":
        multiplication()
    if answer == "division":
        division()        
askoperation()