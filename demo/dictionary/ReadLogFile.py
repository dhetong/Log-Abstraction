from demo.common.Common import tokenGenerator;

def tokenFind(token, DictionaryFile):
    pass;

def dictionarySetUp(logFileName, DictionaryFile):
    logFile = open(logFileName, 'r');
    dictionary = open(DictionaryFile, 'w');
    while 1:
        logLines = logFile.readline(1000000);
        if not logLines:
            break;
        for line in logLines:
            tokens = tokenGenerator(line);
    pass;