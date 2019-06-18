from demo.dictionary.ReadLogFile import dictionarySingleSetUp;
from demo.parsing.MatchLine import tokenMatchSingle;
from demo.dictionary.ReadLogFile import dictionaryDoubleSetUp;
from demo.parsing.MatchLine import tokenMatchDouble;
from demo.dictionary.ReadLogFile import dictionaryTripleSetUp;
from demo.parsing.MatchLine import tokenMatchTriple;

import re;

#dictionarySingleSetUp('Hadoop_2k.txt','SingleDictionary.txt');
#tokenMatchSingle('Hadoop_2k.txt','LogEventSingle.txt','SingleDictionary.txt',3);
#dictionaryDoubleSetUp('Apache.log','DoubleDictionary.txt');
#tokenMatchDouble('Hadoop_2k.txt','LogEventDouble.txt','DoubleDictionary.txt',2);
#dictionaryTripleSetUp('Apache.log','TripleDictionary.txt');
tokenMatchTriple('Apache.log','logEventTriple.txt','TripleDictionary.txt','DoubleDictionary.txt',2,3);


#FTest = open('DoubleDictionary.txt','r');
#Lines = FTest.readlines();
#for line in Lines:
#    line = re.sub('\n','',line)
#    tmp = line.split(',');
#    print(tmp[2]);