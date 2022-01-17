sentence = input("Enter a sentence:")
def findcode( sentence ):
    if sentence == "A":
        code = "0000001"
    elif sentence == "B":
        code = "0000010"
    elif sentence == "C":
        code = "100001"
    elif sentence == "D":
        code = "0000011"
    elif sentence == "E":
        code = "0000101"
    elif sentence == "F":
        code = "0000110"
    elif sentence == "G":
        code = "0000111"
    elif sentence == "H":
        code = "100010"
    elif sentence == "I":
        code = "100011"
    elif sentence == "J":
        code = "0001000"
    elif sentence == "K":
        code = "0001001"
    elif sentence == "L":
        code = "100100"
    elif sentence == "M":
        code = "100101"
    elif sentence == "N":
        code = "100110"
    elif sentence == "O":
        code = "0001010"
    elif sentence == "P":
        code = "0001011"
    elif sentence == "Q":
        code = "0001100"
    elif sentence == "R":
        code = "100111"
    elif sentence == "S":
        code = "101000"
    elif sentence == "T":
        code = "101001"
    elif sentence == "U":
        code = "0001101"
    elif sentence == "V":
        code = "0001110"
    elif sentence == "W":
        code = "0001111"
    elif sentence == "X":
        code = "0010000"
    elif sentence == "Y":
        code = "0010001"
    elif sentence == "Z":
        code = "0010010"
    elif sentence == "a":
        code = "101010"
    elif sentence == "b":
        code = "0010011"
    elif sentence == "c":
        code = "0010100"
    elif sentence == "d":
        code = "101011"
    elif sentence == "e":
        code = "101100"
    elif sentence == "f":
        code = "0010110"
    elif sentence == "g":
        code = "0010111"
    elif sentence == "h":
        code = "101101"
    elif sentence == "i":
        code = "101110"
    elif sentence == "j":
        code = "0011000"
    elif sentence == "k":
        code = "0011001"
    elif sentence == "l":
        code = "101111"
    elif sentence == "m":
        code = "110000"
    elif sentence == "n":
        code = "110001"
    elif sentence == "o":
        code = "110010"
    elif sentence == "p":
        code = "0011010"
    elif sentence == "q":
        code = "0011011"
    elif sentence == "r":
        code = "110011"
    elif sentence == "s":
        code = "110100"
    elif sentence == "t":
        code = "110101"
    elif sentence == "u":
        code = "110110"
    elif sentence == "v":
        code = "0011100"
    elif sentence == "w":
        code = "0011101"
    elif sentence == "x":
        code = "0011110"
    elif sentence == "y":
        code = "0011111"
    elif sentence == "z":
        code = "0100000"
    elif sentence == "\n":
        code = "0100101"
    elif sentence == ".":
        code = "110111"
    elif sentence == ",":
        code = "111000"
    elif sentence == "-":
        code = "0100001"
    elif sentence == "!":
        code = "0100010"
    elif sentence == " ":
        code = "111001"
    elif sentence == "'":
        code = "0100100"
    elif sentence == '"':
        code = "0100011"
    else:
        code = "1111"
    return code

my_string = sentence
my_ans = ""
# print (len(my_string))
for i in range(0,len(my_string)):
    val = findcode(my_string[i])
    my_ans = my_ans + val
print(len(my_ans),".",my_ans)

findcode(sentence)