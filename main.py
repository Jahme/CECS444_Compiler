# James Chomchan Gojit, ID:015785846 - CSULB CECS 444 Compilers with Professor Anthony Giacalone
# Compiler Project - Main Runtime File
from parser.parse import parse
from scanner.scan import scan

if __name__ == '__main__':
    scanned = scan()
    parsed = parse(scanned)

# QUICK ACCESS FOR CLIPBOARD: C:\Users\jchom\Documents\CSULB\Graduate\Fall 2021\CECS 444\Compiler Project\hardtestcase.txt

