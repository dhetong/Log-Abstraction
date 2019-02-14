from demo.dictionary.ReadLogFile import dictionarySingleSetUp;
from demo.dictionary.ReadLogFile import dictionaryDoubleSetUp;

dictionarySingleSetUp('Hadoop_2k.txt','SingleDictionary.txt');
dictionaryDoubleSetUp('Hadoop_2k.txt','DoubleDictionary.txt');

#FTest = open('Hadoop_2k.txt','r');
#Lines = FTest.readlines(1000000);
#for line in Lines:
#   print(line);