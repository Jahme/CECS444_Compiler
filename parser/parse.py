from parser import parser_token
from parser import parse_table

def parse(scan_output):
    # Logging
    new_filename = "parser_log.txt"
    new_file = open(new_filename, "w")  # Will overwrite existing log

    # FILTER
    filtration(scan_output, 'comment')
    filtration(scan_output, 'whspace')
    # DEBUG
    #print(scan_output)

    pvals = []
    stack = [1]
    counter = 0

    # Create parser values
    while counter < len(scan_output):
        pvals.append(parser_token.parser_token.get_token(scan_output[counter]))
        counter += 1
    #DEBUG
    #print(pvals)

    # Reverse
    scan_output.reverse()
    pvals.reverse()
    parser_print = []
    #DEBUG
    #print("Scan Output: ", scan_output)
    #print("PVals: ", pvals)

    while len(pvals) > 0:
        try:
            top = stack[len(stack)-1]
        except:
            try:
                top = stack[0]
            except:
                print("Empty Stack")
                exit(1)
        #print("Top:", top)  # DEBUG

        unit = pvals[len(pvals)-1]
        #print("Unit: ", unit) #DEBUG
        token = scan_output[len(scan_output)-1]
        #print("Scan Output: ", token) #DEBUG


        if top > 0:
            #print("Top: ", top, " - Unit: ", abs(unit))
            from_table = parse_table.parse_table.getvalue(top, abs(unit))
            parser_print = "Fire" + ' ' + str(from_table) + '\n'
            print("Fire" + ' ' + str(from_table))
            new_file.write(parser_print)
            stack.pop()

            #DEBUG
            #print(" FromTable", parser_token.parser_token.get_value(from_table))

            stack.extend(parser_token.parser_token.get_value(from_table))

        elif top <= unit:
            parser_print = "Match and Pop" + ' ' + str(token) + '\n'
            print("Match and Pop" + ' ' + str(token))
            new_file.write(parser_print)
            #print("Stack: ", stack)
            #print("Match and Pop -" + ' ' + str(token) + '\n')


            if token == 'stop':
                parser_print = "Goal" + '\n'
                print("Goal")
                new_file.write(parser_print)
                exit(1)

            stack.pop()
            scan_output.pop()
            pvals.pop()

        else:
            print("It Broke")
            exit(1)

    print(parser_print)
    return parser_print

# Helpers
def filtration(list, value):
    while value in list:
        list.remove(value)