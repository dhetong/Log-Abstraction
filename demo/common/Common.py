import re;

# a function which change the split word to space
def uniSplitWord(logLine):
    #tmp = re.sub(r'-_,\(\)\[\]', " ", logLine);
    tmp = re.sub(r'/(\d{4}[-/]\d{1,2}[-/]\d{1,2})','',logLine);
    tmp = re.sub(r'(\d{4}[-/]\d{1,2}[-/]\d{1,2}\s\d{1,2}:\d{1,2})','',tmp);
    tmp = re.sub(r'-',' ',tmp);
    tmp = re.sub(r'_',' ',tmp);
    tmp = re.sub(r',',' ',tmp);
    tmp = re.sub(r'\[',' ',tmp);
    tmp = re.sub(r'\]',' ',tmp);
    tmp = re.sub(r'\(',' ',tmp);
    tmp = re.sub(r'\)',' ',tmp);
    tmp = re.sub(r'\{',' ',tmp);
    tmp = re.sub(r'\}',' ',tmp);
    tmp = re.sub(r':',' ',tmp);
    tmp = re.sub(r';',' ',tmp);
    tmp = re.sub(r'\.',' ',tmp);
    tmp = re.sub(r'\/',' ',tmp);
    tmp = re.sub(r'[0-9]*','',tmp)
    return tmp;

# a function which is used to modify the log lines
def tokenGenerator(logLine):
    #print(logLine);
    logLineTmp = uniSplitWord(logLine);
    #print(logLineTmp);
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