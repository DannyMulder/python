ascii_letters = {
    "A": [
        "   A   ",
        "  A A  ",
        " A   A ",
        " AAAAA ",
        " A   A "
    ],
    "B": [
        " BBBB  ",
        " B   B ",
        " BBBB  ",
        " B   B ",
        " BBBB  "
    ],
    "C": [
        "  CCCC ",
        " C     ",
        " C     ",
        " C     ",
        "  CCCC "
    ],
    "D": [
        " DDDD  ",
        " D   D ",
        " D   D ",
        " D   D ",
        " DDDD  "
    ],
    "E": [
        " EEEEE ",
        " E     ",
        " EEEE  ",
        " E     ",
        " EEEEE "
    ],
    "F": [
        " FFFFF ",
        " F     ",
        " FFFF  ",
        " F     ",
        " F     "
    ],
    "G": [
        "  GGGG ",
        " G     ",
        " G  GG ",
        " G   G ",
        "  GGG  "
    ],
    "H": [
        " H   H ",
        " H   H ",
        " HHHHH ",
        " H   H ",
        " H   H "
    ],
    "I": [
        " IIIII ",
        "   I   ",
        "   I   ",
        "   I   ",
        " IIIII "
    ],
    "J": [
        " JJJJJ ",
        "     J ",
        "     J ",
        " J   J ",
        "  JJJ  "
    ],
    "K": [
        " K   K ",
        " K  K  ",
        " KKK   ",
        " K  K  ",
        " K   K "
    ],
    "L": [
        " L     ",
        " L     ",
        " L     ",
        " L     ",
        " LLLLL "
    ],
    "M": [
        " M   M ",
        " MM MM ",
        " M M M ",
        " M   M ",
        " M   M "
    ],
    "N": [
        " N   N ",
        " NN  N ",
        " N N N ",
        " N  NN ",
        " N   N "
    ],
    "O": [
        "  OOO  ",
        " O   O ",
        " O   O ",
        " O   O ",
        "  OOO  "
    ],
    "P": [
        " PPPP  ",
        " P   P ",
        " PPPP  ",
        " P     ",
        " P     "
    ],
    "Q": [
        "  QQQ  ",
        " Q   Q ",
        " Q   Q ",
        " Q  Q  ",
        "  QQ Q "
    ],
    "R": [
        " RRRR  ",
        " R   R ",
        " RRRR  ",
        " R  R  ",
        " R   R "
    ],
    "S": [
        "  SSSS ",
        " S     ",
        "  SSS  ",
        "     S ",
        " SSSS  "
    ],
    "T": [
        " TTTTT ",
        "   T   ",
        "   T   ",
        "   T   ",
        "   T   "
    ],
    "U": [
        " U   U ",
        " U   U ",
        " U   U ",
        " U   U ",
        "  UUU  "
    ],
    "V": [
        " V   V ",
        " V   V ",
        " V   V ",
        "  V V  ",
        "   V   "
    ],
    "W": [
        " W   W ",
        " W   W ",
        " W W W ",
        " WW WW ",
        " W   W "
    ],
    "X": [
        " X   X ",
        "  X X  ",
        "   X   ",
        "  X X  ",
        " X   X "
    ],
    "Y": [
        " Y   Y ",
        "  Y Y  ",
        "   Y   ",
        "   Y   ",
        "   Y   "
    ],
    "Z": [
        " ZZZZZ ",
        "    Z  ",
        "   Z   ",
        "  Z    ",
        " ZZZZZ "
    ],
    ":": [
        "      ",
        "  ::  ",
        "      ",
        "  ::  ",
        "      "
    ],
    "!": [
        "  ::  ",
        "  ::  ",
        "  ::  ",
        "      ",
        "  ::  "
]
}

def print_big_word(word):
    word = word.upper()
    for i in range(5):
        line = ""
        for letter in word:
            if letter in ascii_letters:
                line += ascii_letters[letter][i] + "  "
            else:
                line += "      "
        print(line)
