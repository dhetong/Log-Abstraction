import re;

# a function which change the split word to space
def uniSplitWord(logLine):
    tmp = re.sub(r'-_\(\)\[\]', " ", logLine);
    return tmp;

# a function which is used to modify the log lines
def tokenGenerator(logLine):
    logLineTmp = uniSplitWord(logLine);
    tokenList = logLineTmp.split( );
    return tokenList;

# a function which remove the timestamps from a log line
def removeTimestamp():
    pass;

# a function which is used to remove the email address in the log line
def removeEmailAdress():
    pass;

# a function which remove the stopwords from a log line
def removeStopword(logLine, ref):
    pass;