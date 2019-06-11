

from flask import Flask

from flask import Blueprint
main = Flask(__name__)

import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from uuid import uuid1
import json

from demo.dictionary.ReadLogFile import dictionarySingleSetUp;
from demo.parsing.MatchLine import tokenMatchSingle;
from demo.dictionary.ReadLogFile import dictionaryDoubleSetUp;
from demo.parsing.MatchLine import tokenMatchDouble;
from demo.dictionary.ReadLogFile import dictionaryTripleSetUp;
from demo.parsing.MatchLine import tokenMatchTriple;

#@main.route("/Downloads", methods=["GET","POST"])
#def run_Singledictionary():
#dictionarySingleSetUp('Zookeeper.log','SingleDictionaryzoo.txt');

#@main.route("/Downloads", methods=["GET","POST"])
#def run_doubledictionary():
#dictionaryDoubleSetUp('Zookeeper.log','DoubleDictionaryzoo.txt');


#@main.route("/Downloads", methods=["GET","POST"])
#def run_tripledictionary():
#dictionaryTripleSetUp('Zookeeper.log','TripleDictionaryzoo.txt');

#@main.route("/", methods = ["POST"])
#def run_MatchSingle():
#tokenMatchSingle('Zookeeper.log','LogEventSingle.txt','SingleDictionaryzoo.txt',3);

#@main.route("/", methods = ["POST"])
#def run_MatchDouble():
#tokenMatchDouble('Zookeeper.log','LogEventDouble.txt','DoubleDictionaryzoo.txt',2);

@main.route("/", methods = ["GET", "POST"])
def updating():
    sc = SparkContext(appName="PysparkStreaming")
    ssc = StreamingContext(sc, 3)

    lines = ssc.textFileStream('logEventTriplezoo.txt')
    #tokenMatchTriple('Zookeeper.log', 'logEventTriplezoo.txt', 'TripleDictionaryzoo.txt', 'DoubleDictionaryzoo.txt', 2,3)
    count = lines.flatMapValues()
    ssc.start()
    ssc.awaitTermination()


#sc = SparkContext("tt[2]")
#ssc = StreamingContext(sc, 20)
#lines = ssc.socketTextStream("localhost", 9999)
#words = lines.flatMap(lambda line: line.split(" "))


if __name__ == "__main__":
    main.run()
