Source and Log Files for the scanner are found in this folder.\
The requested FSAs are found in the /dfa/ folder.

Notes on each file:
- scan.py: Main executable for the scanner. Interface with program using a command line.
- state.py: Contains state table for the scanner.
- action.py: Contains action table for the scanner.
- lookup.py: Contains lookup table for the scanner.
- token_resolver.py: Used to convert lexemes to tokens.
- token_builder.py: Used to process character input from file to a format usable by the scanner and its tables.
- rwords.txt: Reserved words text file. Necessary to be in same folder as scan.py.
- hardtestcase.txt & big_test.txt: Provided test case files which can be used when running the executable by specifying the filepath.

The screenshots of the logs for the scanner are found in the /logs/ folder.
