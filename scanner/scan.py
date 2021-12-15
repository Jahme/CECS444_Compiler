# James Chomchan Gojit, ID:015785846 - Scan
# This is the main executable serving as the scanner.
from scanner.state import StateTable
from scanner.action import ActionTable
from scanner.lookup import LookupTable
from scanner.token_resolver import *
from scanner.token_builder import TokenBuilder

def scan():
    # File To Scan
    filename = input("Enter file path: ")  # Request file name/path
    #whspace_mode = input("Enter 1 to include white-space. Otherwise, no white-space scan ")
    whspace_mode = 1
    # Logging
    new_filename = "scanner_log.txt"
    new_file = open(new_filename, "w")  # Will overwrite existing log
    write2file = "SCAN: " + filename + "\n"
    new_file.write(write2file)
    # Preparing Reserved Words File
    rword_file = "rwords.txt"
    f = open(filename, "r")
    reserved = open(rword_file, "r").readlines()
    rword_comp = [word.strip() for word in reserved]

    # Variables
    state = 0
    action = 0
    lookahead = 0
    current_token = ""
    scanned_tokens = []

    # Scan Loop until EOF
    while 1:
        character = f.read(1)  # Read in a single character from filestream
        select = TokenBuilder.build_token(character)  # Translate character to readable for state table
        action = ActionTable.get_action(state, select)  # Retrieve from action table
        lookahead = StateTable.get_next_state(state, select)  # Potential new state
        if lookahead != -1 and action == 2:  # Move Append
            current_token += character
            state = lookahead
        elif lookahead != -1 and action == 3:  # Move No Append
            state = lookahead
        elif lookahead == -1 and action == 6:  # Halt Reuse - Create token
            # Check if reserved word
            token_id = get_token_id(LookupTable.lookup(state, select))

            if token_id == "id" and (current_token in rword_comp):
                stringPrint = "RESERVED WORD: " + current_token + " - IDENTIFIER"
                scanned_tokens.append(current_token)
                #print(stringPrint)  # For console print
                new_file.write(stringPrint + "\n")  # For logging
            else:
                if whspace_mode == "1":  # Whitespace Mode
                    stringPrint = 'TOKEN: {:>11} - '.format(token_id) + current_token + ""
                    scanned_tokens.append(token_id)
                    #print(stringPrint)  # For console print
                    new_file.write(stringPrint + "\n")  # For logging
                else:  # No whitespace mode
                    if token_id != "whspace":
                        stringPrint = 'TOKEN: {:>11} - '.format(token_id) + current_token + ""
                        scanned_tokens.append(token_id)
                        #print(stringPrint)  # For console print
                        new_file.write(stringPrint + "\n")  # For logging
            state = 0  # Reset State
            state = StateTable.get_next_state(state, select)  # Go into Next
            if character != '\n':  # Escape Character
                current_token = character
            else:
                current_token = ""
        if not character:  # End of File Read
            break

    return scanned_tokens

if __name__ == "__main__":
    result = scan()
    for element in result:
        print(element)