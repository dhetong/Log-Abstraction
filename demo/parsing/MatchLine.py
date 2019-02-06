from demo.common.Common import tokenGenerator;

#the function which is used to detect dynamic and static parts based on single token
def singleTokenCompare(logTokens, tokenFile, threshold, outputFile):
    for token in logTokens:
        while 1:
            tokenList = tokenFile.readlines(100000);
            findIdentifier = False;
            if not tokenList:
                if not findIdentifier:
                    token = '#';
                break;
            for tokenItem in tokenList:
                if token in tokenItem:
                    findIdentifier = True;
                    tmp = tokenItem.split(',');
                    frequency = int(tmp[1]);
                    if frequency >= threshold:
                        pass;
                    else:
                        token = '#'
                    break;
            if findIdentifier:
                break;

def tokenMatch(inputLogFile, outputEventFile, tokenFile):
    #open the input log files, output log event files and the token dictionary
    try:
        inFile = open(inputLogFile, 'r');
        outFile = open(outputEventFile, 'w');
        tokenFile = open(tokenFile, 'r');

        while 1:
            logLines = inFile.readlines(100000);
            if not logLines:
                break;
            for logLine in logLines:
                logTokens = tokenGenerator(logLine);
                pass;

    finally:
        if inFile and outFile and tokenFile:
            inFile.close();
            outFile.close();
            tokenFile.close();
    pass;