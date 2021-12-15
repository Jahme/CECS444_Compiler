class parser_token:
    terminals = [0, "library", "program", "id", ";", ":", ",", "int", "sci", "real", "currency", "string", "begin", "return",
                 ":=", "for", "to", "do", "end", "var", "repeat", "until", "while", "(", ")", "if", "then", "else", "device_open", "device_close", "file",
                 "read_from_device", "write_to_device", "writeln", "readln", "<", ">", "<=", ">=", "==", "!=", "+", "-",
                 "*", "/", "abs", "fabs", "stop", "$"]

    dict = {
         1: [4, 2, 3],
         2: [4],
         3: [2, 3],
         5: [-1],
         6: [5],
         8: [23, 12, 6, -4, -3, -2],
         9: [7, -4, 11, -5, 8, -19],
        10: [7, -4, 11, -5, 8],
        12: [9, 10],
        13: [9, 10, -6],
        15: [-3],
        16: [-7],
        17: [-8],
        18: [-9],
        19: [-10],
        20: [-11],
        21: [-4, -7, -13, 13, -12],
        22: [14, 15],
        23: [14, 15],
        25: [-4, 18, -14, -3],
        26: [-4, -30, -28],
        27: [-4, -17, -18, 13, -17, -3, -16, -3, -14, -3, -15],
        28: [-4, -17, -18, -24, 16, -23, -21, 13, -17, -20],
        29: [-4, -17, -18, 13, -17, -24, 16, -23, -22],
        30: [-4, -18, 13, -12, -27, -4, -18, 13, -12, -26, -24, 16, -23, -25],
        31: [-4, -30, -29],
        32: [-4, -30, -31],
        33: [-4, -30, -32],
        34: [-4, -24, 18, -23, -33],
        35: [-4, -24, 8, -23, -34],
        36: [18, 18, 18],
        37: [-35],
        38: [-36],
        39: [-37],
        40: [-38],
        41: [-39],
        42: [-40],
        43: [19, 20],
        44: [-11],
        45: [19, 20, -41],
        46: [19, 20, -42],
        48: [21, 22],
        49: [21, 22, -43],
        50: [21, 22, -44],
        52: [-24, 18, -23],
        53: [-3],
        54: [-7],
        55: [-9],
        56: [-8],
        57: [-10],
        58: [-24, 18, -23, -45],
        59: [-24, 18, -23, -46],
        60: [-47]
    }

    def get_token(token):
        try:
            token_value = parser_token.terminals.index(token)
        except:
            return 0

        return token_value * -1 #Negative indexing

    def get_value(token):
        if token == 0:
            print("Read Error")
            exit(1)
        elif token == 61:
            print("Scan Error")
            exit(1)
        elif token == 62:
            print("Pop Error")
            exit(1)

        try:
            parser_val = parser_token.dict[token]
        except:
            return []

        return parser_val

if __name__ == "__main__":
    print(len(parser_token.terminals))
    print(parser_token.terminals.index(':'))

