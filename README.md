# CECS444_Compiler
Fall 2021 CECS 444 @ CSULB Semester Project - Compiler: Scanner and Parser\
Author: James Chomchan Gojit - CSULB

## Quick Access
[Runtime File](main.py)\
[Parser Class](/parser/parse.py)\
[Scanner Class](/scanner/scan.py)\
[Parser Logs](/parser/logs/Parser_Output.pdf)\
[Predict Set](/parser/sets_tables/PredictSet.png)\
[First and Follow Sets](/parser/sets_tables/FirstSet_FollowSet.png)

## Scanner
Raw files from my local repository are organized in the /scanner/ folder.\
[FSA Images and Logs File](FSAs_Logs.pdf) Note: This file does not include the Full DFA, which is provided separately.\
[Full DFA Image](Scanner_FullDFA.png)

## Parser
Raw files from my local repository are organized in the /parser/ folder.\
The runtime file [Runtime File](main.py). However, this file is just a wrapper of the parse and scan classes.\
To quickly explain, the runtime file functions by running the scan() method from the scanner class. The output of this is passed into the parse() method of the parser class.\
You can find the standalone parser here: [Parser File](/parser/parse.py)

## Notes
In regard to the [grammar](grammar.txt) provided, some changes were made to clarify understanding of how the program should be interpreted. 
- The original non-terminal production "end -> stop" and the "end" found in the loops of production "statement -> ..." were a bit confusing. The changes made were made under the belief that the "end" found in the loops were the reserved word "end".\
- The production "code -> program" conflicted with the start production "program -> libtoken ...". As such, the starting production was renamed to "goal" under observation of the original grammar found in the instructor's repository.\
- The production "var -> id" and the FIRST(vars) = var could have resolved just fine. Through observation of the [test case](hardtestcase.txt), it is believed that the var found in the "vars ->" production is a reserved word, and is thus included as a terminal character.
- I should probably create a test case implementing the loops of the grammar.
