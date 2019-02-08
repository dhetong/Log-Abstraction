from demo.common.Common import tokenGenerator;

def dictionarySingleSetUp(logFileName, DictionaryFileName):
    logFile = open(logFileName, 'r');
    dictionaryFile = open(DictionaryFileName, '+');
    dictionaryList = {'dictionaryDHT': -1};
    while 1:
        logLines = logFile.readline(1000000);
        if not logLines:
            break;
        for line in logLines:
            tokens = tokenGenerator(line);
            for token in tokens:
                if dictionaryList.has_key(token):
                    dictionaryList[token] = dictionaryList[token] + 1;
                else:
                    dictionaryList[token] = 1;
    dictionaryKey = dictionaryList.keys();
    for key in dictionaryKey:
        dictionaryFile.writeline(key + ',' + str(dictionaryList[key]));
    pass;

def dictionaryDoubleSetUp(logFileName, DictionaryFileName):
    logFile = open(logFileName, 'r');
    dictionaryFile = open(DictionaryFileName, 'r');
    dictionaryList = {'dictionaryDHT': -1};

    while 1:
        logLines = logFile.readlines(1000000);
        if not logLines:
            break;
        for line in logLines:
            tokens = tokenGenerator(line);
            for index in range(len(tokens)):
                if index == len(tokens)-1:
                    break;
                else:
                    pass;
    pass;