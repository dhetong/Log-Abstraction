from demo.common.Common import tokenGenerator;

#the function which is used to detect dynamic and static parts based on single token
def singleTokenCompare(logTokens, tokenDictionary, threshold, outputFile):
    for token in logTokens:
        if tokenDictionary[token] >= threshold:
            pass;
        else:
            token = '#';
    return logTokens;

def tokenMatchSingle(inputLogFile, outputEventFile, tokenDicFile):
    #open the input log files, output log event files and the token dictionary
    try:
        inFile = open(inputLogFile, 'r');
        outFile = open(outputEventFile, 'w');
        tokenFile = open(tokenDicFile, 'r');
        tokenDictionary = {'dictionaryDHT':-1};

        tokenLines = tokenFile.readlines();
        for tokenLine in tokenLines:
            tmp = tokenLine.split(',');
            tokenDictionary[tmp[0]] = int(tmp[1]);

        while 1:
            logLines = inFile.readlines(100000);
            if not logLines:
                break;
            for logLine in logLines:
                logTokens = tokenGenerator(logLine);

    finally:
        if inFile and outFile and tokenFile:
            inFile.close();
            outFile.close();
            tokenFile.close();

def doubleTokenCompare(tokenLines, tokenDictionary, threshold, outputFile):
    pass;

def tokenMatchDouble(inputFile, outputFile, tokenDicFile):
    try:
        inFile = open(inputFile, 'r');
        outFile = open(outputFile, 'w');
        tokenFile = open(tokenDicFile, 'r');
        tokenDictionary = {'dictionary', -1};
    finally:
        if inFile and outFile and tokenFile:
            inFile.close();
            outFile.close();
            tokenFile.close();