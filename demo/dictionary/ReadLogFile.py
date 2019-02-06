from demo.common.Common import tokenGenerator;

def tokenFind(token, dictionaryFile):
    find = False;
    while 1:
        tokenLines = dictionaryFile.readline(1000000);
        if not tokenLines:
            if not find:
                dictionaryFile.writeline(token + ',1');
            break;
        for line in tokenLines:
            if token in line:
                find = True;
                tmp = line.split(',');
                frequency = int(tmp[1]);
                frequency = frequency + 1;
                line = line.replace(tmp[1], str(frequency));
                dictionaryFile.writeline(line);
                break;
        if find:
            break;

def dictionarySetUp(logFileName, DictionaryFileName):
    logFile = open(logFileName, 'r');
    dictionaryFile = open(DictionaryFileName, '+');
    while 1:
        logLines = logFile.readline(1000000);
        if not logLines:
            break;
        for line in logLines:
            tokens = tokenGenerator(line);
            for token in tokens:
                tokenFind(token, dictionaryFile);
    pass;