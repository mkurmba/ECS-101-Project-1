binary = input("Enter a binary: ")
def longchar():
    char = " "
    if binary[i:i+7] == "0000001":
        char = "A"
    elif binary[i:i + 7] == "0000010":
        char = "B"
    elif binary[i:i + 7] == "0000011":
        char = "D"
    elif binary[i:i + 7] == "0000101":
        char = "E"
    elif binary[i: i + 7] == "0000110":
        char = "F"
    elif binary[i: i + 7] == "0000111":
        char = "G"
    elif binary[i: i + 7] == "0001000":
        char = "J"
    elif binary[i: i + 7] == "0001001":
        char = "K"
    elif binary[i: i + 7] == "0001010":
        char = "O"
    elif binary[i: i + 7] == "0001011":
        char = "P"
    elif binary[i: i + 7] == "0001100":
        char = "Q"
    elif binary[i: i + 7] == "0001101":
        char = "U"
    elif binary[i: i + 7] == "0001110":
        char = "V"
    elif binary[i: i + 7] == "0001111":
        char = "W"
    elif binary[i: i + 7] == "0010000":
        char = "X"
    elif binary[i: i + 7] == "0010001":
        char = "Y"
    elif binary[i: i + 7] == "0010010":
        char = "Z"
    elif binary[i: i + 7] == "0010011":
        char = "b"
    elif binary[i: i + 7] == "0010100":
        char = "c"
    elif binary[i: i + 7] == "0010110":
        char = "f"
    elif binary[i: i + 7] == "0010111":
        char = "g"
    elif binary[i: i + 7] == "0011000":
        char = "j"
    elif binary[i: i + 7] == "0011001":
        char = "k"
    elif binary[i: i + 7] == "0011010":
        char = "p"
    elif binary[i: i + 7] == "0011011":
        char = "q"
    elif binary[i: i + 7] == "0011100":
        char = "v"
    elif binary[i: i + 7] == "0011101":
        char = "w"
    elif binary[i: i + 7] == "0011110":
        char = "x"
    elif binary[i: i + 7] == "0011111":
        char = "y"
    elif binary[i: i + 7] == "0100000":
        char = "z"
    elif binary[i: i + 7] == "0100001":
        char = "-"
    elif binary[i: i + 7] == "0100010":
        char = "!"
    elif binary[i: i + 7] == "0100011":
        char = "“"
    elif binary[i: i + 7] == "0100100":
        char = "'"
    elif binary[i: i + 7] == "0100101":
        char = "\n"
    print(char,end='')
def shortchar():
    char = " "
    if binary[i: i + 6] == "100001":
        char = "C"
    elif binary[i: i + 6] == "100010":
        char = "H"
    elif binary[i: i + 6] == "100011":
        char = "I"
    elif binary[i: i + 6] == "100100":
        char = "L"
    elif binary[i: i + 6] == "100101":
        char = "M"
    elif binary[i: i + 6] == "100110":
        char = "N"
    elif binary[i: i + 6] == "100111":
        char = "R"
    elif binary[i: i + 6] == "101000":
        char = "S"
    elif binary[i: i + 6] == "101001":
        char = "T"
    elif binary[i: i + 6] == "101010":
        char = "a"
    elif binary[i: i + 6] == "101011":
        char = "d"
    elif binary[i: i + 6] == "101100":
        char = "e"
    elif binary[i: i + 6] == "101101":
        char = "h"
    elif binary[i: i + 6] == "101110":
        char = "i"
    elif binary[i: i + 6] == "101111":
        char = "l"
    elif binary[i: i + 6] == "110000":
        char = "m"
    elif binary[i: i + 6] == "110001":
        char = "n"
    elif binary[i: i + 6] == "110010":
        char = "o"
    elif binary[i: i + 6] == "110011":
        char = "r"
    elif binary[i: i + 6] == "110100":
        char = "s"
    elif binary[i: i + 6] == "110101":
        char = "t"
    elif binary[i: i + 6] == "110110":
        char = "u"
    elif binary[i: i + 6] == "110111":
        char = "."
    elif binary[i: i + 6] == "111000":
        char = ","
    elif binary[i :i + 6] == "111001":
        char = " "
    print(char,end='')

i = 0
while(i<len(binary)):
    if binary[i] == "0":
        longchar()
        i = i+7
    elif binary[i] == "1":
        shortchar()
        i = i+6
print(" ")