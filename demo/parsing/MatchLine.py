import re;

from demo.common.Common import tokenGenerator;

#the function which is used to detect dynamic and static parts based on single token
def singleTokenCompare(logTokens, tokenDictionary, threshold):
    logEvent = '';
    for token in logTokens:
        if token in tokenDictionary:
            #print(token);
            if tokenDictionary[token] >= threshold:
                pass;
            else:
                token = '#';
        else:
            token = '#';
        logEvent = logEvent + token + ' ';
    return logEvent;

def tokenMatchSingle(inputLogFile, outputEventFile, tokenDicFile, threshold):
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
                logEvent = singleTokenCompare(logTokens,tokenDictionary,threshold);
                logEvent = re.sub(r'^[0-9]+','#',logEvent);
                logEvent = re.sub(r'[ ][0-9]+',' #',logEvent);
                outFile.write(logEvent);
                outFile.write('\n');


    finally:
        if inFile and outFile and tokenFile:
            inFile.close();
            outFile.close();
            tokenFile.close();

def doubleTokenCompare(logTokens, tokenDictionary, threshold):
    logEvent = '';
    for index in range(len(logTokens)):
        if index == len(logTokens) - 1:
            break;
        doubleTmp = logTokens[index] + ',' + logTokens[index+1];
        if doubleTmp in tokenDictionary and tokenDictionary[doubleTmp] >= threshold:
            token = logTokens[index];
        else:
            if index > 0:
                doubleTmp = logTokens[index - 1] + ',' + logTokens[index];
                if doubleTmp in tokenDictionary and tokenDictionary[doubleTmp] >= threshold:
                    token = logTokens[index];
                else:
                    token = '#';
            else:
                token = '#';
        logEvent = logEvent + token + ' ';
    return logEvent;

def tokenMatchDouble(inputFile, outputFile, tokenDicFile, threshold):
    try:
        inFile = open(inputFile, 'r');
        outFile = open(outputFile, 'w');
        tokenFile = open(tokenDicFile, 'r');
        tokenDictionary = {'dictionary':-1};

        tokenLines = tokenFile.readlines();
        for tokenLine in tokenLines:
            tokenLine = re.sub('\n', '', tokenLine);
            tmp = tokenLine.split(',');
            keyTmp = tmp[0] + ',' + tmp[1];
            tokenDictionary[keyTmp] = int(tmp[2]);

        while 1:
            logLines = inFile.readlines(100000);
            if not logLines:
                break;
            for logLine in logLines:
                logTokens = tokenGenerator(logLine);
                logEvent = doubleTokenCompare(logTokens,tokenDictionary,threshold);
                logEvent = re.sub(r'^[0-9]+', '#', logEvent);
                logEvent = re.sub(r'[ ][0-9]+',' #', logEvent);
                outFile.write(logEvent);
                outFile.write('\n');

    finally:
        if inFile and outFile and tokenFile:
            inFile.close();
            outFile.close();
            tokenFile.close();

def doubleTokenCheck(logTokens, indexList):
    pass;

def removeRepeat(indexList):
    pass;

def tripleTokenCompare(logTokens, tokenDictionary, threshold):
    logEvent = '';
    dynamicIndex = [];
    checkTokenList = [];
    for index in range(len(logTokens)):
        if index == len(logTokens) - 2:
            break;
        tripleTmp = logTokens[index] + ',' + logTokens[index+1] + ',' + logTokens[index+2];
        if tripleTmp in tokenDictionary and tokenDictionary[tripleTmp] >= threshold:
            pass;
        else:
            checkTokenList.extend([index,index+1,index+2]);
        pass;
    pass;

def tokenMatchTriple(inputFile, outputFile, tokenDicFile, threshold):
    try:
        inFile = open(inputFile, 'r');
        outFile = open(outputFile, 'w');
        tokenFile = open(tokenDicFile, 'r');
        tokenDictionary = {'dictionary':-1};

        tokenLines = tokenFile.readlines();
        for tokenLine in tokenLines:
            tokenLine = re.sub('\n', '', tokenLine);
            tmp = tokenLine.split(',');
            keyTmp = tmp[0] + ',' + tmp[1] + ',' + tmp[2];
            tokenDictionary[keyTmp] = int(tmp[3]);

        while 1:
            logLines = inFile.readlines(100000);
            if not logLines:
                break;
            for logLine in logLines:
                logTokens = tokenGenerator(logLine);
                logEvent = tripleTokenCompare(logTokens,tokenDictionary,threshold);
                logEvent = re.sub(r'^[0-9]+', '#', logEvent);
                logEvent = re.sub(r'[ ][0-9]+',' #', logEvent);
                outFile.write(logEvent);
                outFile.write('\n');

    finally:
        if inFile and outFile and tokenFile:
            inFile.close();
            outFile.close();
            tokenFile.close();
    pass;