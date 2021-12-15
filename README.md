# CECS444_Compiler
Fall 2021 CECS 444 @ CSULB Semester Project - Compiler: Scanner and Parser\
Author: James Chomchan Gojit - CSULB

## Quick Access
[Runtime File](main.py)\
[Parser Class](/parser/parse.py)\
[Scanner Class](/scanner/scan.py)\
[Parser Logs](/parser/logs/Parser_Output.pdf)
[Tables](/parser/sets_and_tables/)

## Scanner
Raw files from my local repository are organized in the /scanner/ folder.\
[FSA Images and Logs File](FSAs_Logs.pdf) Note: This file does not include the Full DFA, which is provided separately.\
[Full DFA Image](Scanner_FullDFA.png)

## Parser
Raw files from my local repository are organized in the /parser/ folder.\
The runtime file [Runtime File](main.py). However, this file is just a wrapper of the parse and scan classes.\
To quickly explain, the runtime file functions by running the scan() method from the scanner class. The output of this is passed into the parse() method of the parser class.\
You can find the standalone parser here: [Parser File](/parser/parse.py)
