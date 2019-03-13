from demo.common.Common import tokenGenerator;

def dictionarySingleSetUp(logFileName, DictionaryFileName):
    logFile = open(logFileName, 'r');
    dictionaryFile = open(DictionaryFileName, 'w+');
    dictionaryList = {'dictionaryDHT': -1};
    while 1:
        logLines = logFile.readlines(1000000);
        if not logLines:
            break;
        for line in logLines:
            tokens = tokenGenerator(line);
            for token in tokens:
                if token in dictionaryList:
                    dictionaryList[token] = dictionaryList[token] + 1;
                else:
                    dictionaryList[token] = 1;
    dictionaryKey = dictionaryList.keys();
    for key in dictionaryKey:
        dictionaryFile.write(key + ',' + str(dictionaryList[key]));
        dictionaryFile.write('\n');
    pass;

def dictionaryDoubleSetUp(logFileName, DictionaryFileName):
    logFile = open(logFileName, 'r');
    dictionaryFile = open(DictionaryFileName, 'w+');
    dictionaryList = {'dictionary,DHT': -1};

    while 1:
        logLines = logFile.readlines(1000000);
        if not logLines:
            break;
        for line in logLines:
            tokens = tokenGenerator(line);
            for index in range(len(tokens)):
                if index == len(tokens)-1:
                    break;
                doubleTmp = tokens[index] + ',' + tokens[index+1];
                if doubleTmp in dictionaryList:
                    dictionaryList[doubleTmp] = dictionaryList[doubleTmp] + 1;
                else:
                    dictionaryList[doubleTmp] = 1;
    dictionaryKey = dictionaryList.keys();
    for key in dictionaryKey:
        dictionaryFile.write(key + ',' + str(dictionaryList[key]));
        dictionaryFile.write('\n');
    pass;

def dictionaryTripleSetUp(logFileName, DictionaryFileName):
    logFile = open(logFileName, 'r');
    dictionaryFile = open(DictionaryFileName, 'w+');
    dictionaryList = {'dictionary,DHT,triple': -1};

    while 1:
        logLines = logFile.readlines(1000000);
        if not logLines:
            break;
        for line in logLines:
            tokens = tokenGenerator(line);
            for index in range(len(tokens)):
                if index == len(tokens)-2:
                    break;
                tripleTmp = tokens[index] + ',' + tokens[index+1] + ',' + tokens[index+2];
                if tripleTmp in dictionaryList:
                    dictionaryList[tripleTmp] = dictionaryList[tripleTmp] + 1;
                else:
                    dictionaryList[tripleTmp] = 1;
    dictionaryKey = dictionaryList.keys();
    for key in dictionaryKey:
        dictionaryFile.write(key + ',' + str(dictionaryList[key]));
        dictionaryFile.write('\n');
    pass;